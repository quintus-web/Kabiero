from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admission_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=20)
    parent_phone = models.CharField(max_length=15, default='')
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def total_paid(self):
        return sum(payment.amount_paid for payment in self.payment_set.all())

    @property
    def fee_balance(self):
        from finance.models import FeeStructure
        fee = FeeStructure.objects.filter(grade=self.grade).first()
        return fee.total_amount() - self.total_paid if fee else 0

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=[
            ('ADMIN', 'Admin'),
            ('BURSAR', 'Bursar'),
            ('TEACHER', 'Teacher'),
        ]
    )

    def __str__(self):
        return self.user.username