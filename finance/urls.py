from django.urls import path
from .views import student_finance_dashboard, bursar_dashboard, student_balances, mpesa_payment

urlpatterns = [
    path('student/', student_finance_dashboard, name='student-finance'),
    path('bursar/', bursar_dashboard, name='bursar-dashboard'),
    path('balances/', student_balances, name='student-balances'),
    path('mpesa/', mpesa_payment, name='mpesa-payment'),
]