from django.db import models
from accounts.models import Student

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    marks = models.IntegerField()
    term = models.CharField(max_length=20)
    year = models.IntegerField()
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"

    class Meta:
        ordering = ['-date_entered']
