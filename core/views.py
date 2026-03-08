from django.shortcuts import render, redirect

def home(request):
    return render(request, 'publicsource/index.html')

def about(request):
    return render(request, 'publicsource/about.html')

def academics(request):
    return render(request, 'publicsource/academics.html')

def gallery(request):
    return render(request, 'publicsource/gallery.html')

def contact(request):
    return render(request, 'publicsource/contact.html')


def dashboard_router(request):
    user = request.user
    if hasattr(user, 'student'):
        return redirect('student-finance')
    elif hasattr(user, 'staff'):
        return redirect('bursar-dashboard')
    else:
        return redirect('home')


from accounts.models import Student
from finance.models import Payment
from attendance.models import Attendance
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    total_students = Student.objects.count()
    
    total_payments = Payment.objects.aggregate(
        total=Sum('amount_paid')
    )['total'] or 0
    
    attendance_count = Attendance.objects.count()
    
    recent_payments = Payment.objects.all().order_by('-date_paid')[:5]
    
    context = {
        "total_students": total_students,
        "total_payments": total_payments,
        "attendance_count": attendance_count,
        "recent_payments": recent_payments
    }
    
    return render(request, "admin_dashboard.html", context)
