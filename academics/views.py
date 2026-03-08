from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Result
from accounts.models import Student
from .utils import send_results_sms

@login_required
def student_results(request, admission):
    student = get_object_or_404(Student, admission_number=admission)
    results = Result.objects.filter(student=student)
    
    total = sum(r.marks for r in results)
    count = results.count()
    average = round(total / count, 2) if count > 0 else 0
    
    context = {
        "student": student,
        "results": results,
        "average": average,
        "total": total,
        "count": count
    }
    
    return render(request, "academics/results.html", context)

def send_results_to_parent(student, average):
    message = f"""Kabiero School

Results for {student.first_name} {student.last_name}

Average Score: {average}%

Login to portal for full report.
"""
    
    if student.parent_phone:
        send_results_sms(student.parent_phone, message)
        return True
    return False
