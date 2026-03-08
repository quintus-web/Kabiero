from django.urls import path
from .views import student_results

urlpatterns = [
    path('results/<str:admission>/', student_results, name='student-results'),
]
