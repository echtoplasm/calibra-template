from django.shortcuts import render
from django.db import models
from accounts.models import CustomUser
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate

# Create your views here.
user = CustomUser

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = CustomUser.objects.create_user(
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'Username already taken'}, status=400)
        
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request, 
            username=data['username'],
            password=data['password']
        )
        if user is None:
            return JsonResponse({'error': 'User not found'}, status=404)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)
            
