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
    if User.objects.filter(is_superuser=True).exists():
        return JsonResponse({
            'status': 'exists',
            'message': 'Superuser already exists',
            'count': User.objects.filter(is_superuser=True).count()
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
            'password': password
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
