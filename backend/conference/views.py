from django.shortcuts import render
from rest_framework import generics
from .models import VideoConference
from .serializers import ConferenceSerializer

# Create your views here.

class ConferenceList(generics.ListCreateAPIView):
    queryset = VideoConference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VideoConference.objects.all()
    serializer_class = ConferenceSerializer
