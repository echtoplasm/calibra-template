from.models import CustomUser
from rest_framework import response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

# Create your views here.

@csrf_exempt
def login_view(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    user = authenticate(
      request,
      username=data['username'],
      password=data['password'])
    if user is None:
      return JsonResponse(
        {'error': 'unable to login, please check user name and password'},
        status=400)
    else:
      try:
        token = Token.objects.get(user=user)
      except:
        token = Token.objects.create(user=user)
      return JsonResponse({'token': str(token)}, status=201)
    

@csrf_exempt
def signup(request):
  try:
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = CustomUser.objects.create_user(username=data['username'], password=data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return JsonResponse({'token': str(token)}, status=201)
  except IntegrityError:
    return JsonResponse({'error': 'Username already taken'}, status=400)


