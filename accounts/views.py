from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os

def login_view(request):
    """Redirect to admin login"""
    return redirect('/admin/login/')

@csrf_exempt
def init_superuser(request):
    """Emergency superuser creation endpoint"""
    
    # Check if superuser exists
    superusers = User.objects.filter(is_superuser=True)
    if superusers.exists():
        usernames = list(superusers.values_list('username', flat=True))
        return JsonResponse({
            'status': 'exists',
            'message': 'Superuser already exists',
            'count': superusers.count(),
            'usernames': usernames
        })
    
    # Create superuser
    try:
        username = 'admin'
        email = 'admin@kabiero.com'
        password = 'kabiero2025'
        
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        
        return JsonResponse({
            'status': 'created',
            'message': f'Superuser "{username}" created successfully',
            'username': username,
            'password': password,
            'login_url': '/admin/'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
            'total_users': User.objects.count()
        }, status=500)

@csrf_exempt
def check_users(request):
    """Debug endpoint to check existing users"""
    users = User.objects.all()
    superusers = User.objects.filter(is_superuser=True)
    
    return JsonResponse({
        'total_users': users.count(),
        'total_superusers': superusers.count(),
        'superuser_usernames': list(superusers.values_list('username', flat=True)),
        'all_usernames': list(users.values_list('username', flat=True))
    })
