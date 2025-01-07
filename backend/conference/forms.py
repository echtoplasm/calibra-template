from django import forms
from .models import VideoConference

class VideoConferenceAddForm(forms.ModelForm):
    class Meta:
        model = VideoConference
        fields = '__all__'

class VideoConferenceChangeForm(forms.ModelForm):
    class Meta:
        model = VideoConference
        fields = '__all__'
