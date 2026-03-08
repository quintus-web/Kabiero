from django.contrib import admin
from .models import Result
from .views import send_results_to_parent

class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks', 'term', 'year', 'date_entered']
    list_filter = ['term', 'year', 'subject']
    search_fields = ['student__first_name', 'student__last_name', 'student__admission_number']
    actions = ['send_sms_to_parents']
    
    def send_sms_to_parents(self, request, queryset):
        students = set(result.student for result in queryset)
        for student in students:
            results = Result.objects.filter(student=student)
            total = sum(r.marks for r in results)
            count = results.count()
            average = round(total / count, 2) if count > 0 else 0
            send_results_to_parent(student, average)
        self.message_user(request, f"SMS sent to {len(students)} parents")
    
    send_sms_to_parents.short_description = "Send results SMS to parents"

admin.site.register(Result, ResultAdmin)
