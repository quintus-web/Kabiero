from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import Student
from .models import Payment, FeeStructure

@login_required
def student_finance_dashboard(request):
    student = request.user.student

    payments = Payment.objects.filter(student=student)
    total_paid = sum(p.amount_paid for p in payments)

    fee = FeeStructure.objects.filter(grade=student.grade).first()
    total_fees = fee.total_amount() if fee else 0

    balance = total_fees - total_paid

    context = {
        'student': student,
        'payments': payments,
        'total_paid': total_paid,
        'total_fees': total_fees,
        'balance': balance
    }

    return render(request, 'finance/student_dashboard.html', context)
from django.shortcuts import redirect
from .forms import PaymentForm
from accounts.models import Staff

@login_required
def bursar_dashboard(request):
    # Ensure only bursar/admin can access
    if not hasattr(request.user, 'staff'):
        return redirect('dashboard')

    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bursar-dashboard')

    payments = Payment.objects.all().order_by('-date_paid')[:10]

    context = {
        'form': form,
        'payments': payments
    }

    return render(request, 'finance/bursar_dashboard.html', context)


@login_required
def student_balances(request):
    students = Student.objects.all()
    data = []
    
    for student in students:
        payments = Payment.objects.filter(student=student)
        total_paid = sum(p.amount_paid for p in payments)
        fee = FeeStructure.objects.filter(grade=student.grade).first()
        total_fees = fee.total_amount() if fee else 0
        balance = total_fees - total_paid
        
        data.append({
            "student": student,
            "paid": total_paid,
            "balance": balance
        })
    
    return render(request, "finance/student_balances.html", {"data": data})


def mpesa_payment(request):
    if request.method == "POST":
        admission = request.POST.get("admission")
        amount = request.POST.get("amount")
        phone = request.POST.get("phone")
        
        try:
            student = Student.objects.get(admission_number=admission)
            
            Payment.objects.create(
                student=student,
                amount_paid=amount,
                payment_method="MPESA",
                reference=f"MPESA-{phone}"
            )
            
            return redirect("student-finance")
        except Student.DoesNotExist:
            return render(request, "finance/mpesa_payment.html", {"error": "Student not found"})
    
    return render(request, "finance/mpesa_payment.html")
