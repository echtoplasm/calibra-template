from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Notification
from api.serializers import NotificationSerializer
# Create your views here.

class NotificationList(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.AllowAny,)

class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.AllowAny,)

