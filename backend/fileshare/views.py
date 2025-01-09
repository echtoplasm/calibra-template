from django.shortcuts import render
from rest_framework import generics
from .models import File, FileAccess
from api.serializers import FileSerializer, FileAccessSerializer

# Create your views here.

class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileAccessList(generics.ListCreateAPIView):
    queryset = FileAccess.objects.all()
    serializer_class = FileAccessSerializer

class FileAccessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FileAccess.objects.all()
    serializer_class = FileAccessSerializer
