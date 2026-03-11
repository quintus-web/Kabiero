from django.urls import path
from . import views

urlpatterns = [
    # example login page
    path("login/", views.login_view, name="login"),
]