from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    data = request.data
    try:
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            first_name=data['fullName']
        )
        return JsonResponse({'username': user.username, 'fullName': user.first_name, 'email': user.email}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@api_view(['POST'])
def login(request):
    data = request.data
    user = authenticate(username=data['username'], password=data['password'])
    if user is not None:
        return JsonResponse({'username': user.username, 'fullName': user.first_name, 'email': user.email}, status=200)
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=400)
