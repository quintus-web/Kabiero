from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("init-superuser/", views.init_superuser, name="init-superuser"),
    path("check-users/", views.check_users, name="check-users"),
]