from rest_framework import serializers
from .models import VideoConference

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoConference
        fields = '__all__'

