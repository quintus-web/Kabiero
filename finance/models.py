from django.db import models
from accounts.models import Student

class FeeStructure(models.Model):
    grade = models.CharField(max_length=20)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    transport_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lunch_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    term = models.CharField(max_length=20)
    year = models.IntegerField()

    def total_amount(self):
        return self.tuition_fee + self.transport_fee + self.lunch_fee

    def __str__(self):
        return f"{self.grade} - {self.term} {self.year}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('CASH', 'Cash'),
            ('MPESA', 'MPESA'),
            ('BANK', 'Bank'),
        ]
    )
    reference = models.CharField(max_length=50, blank=True)
    date_paid = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.amount_paid}"