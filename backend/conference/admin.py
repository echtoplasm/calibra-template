from django.contrib import admin
from .models import VideoConference
from .forms import VideoConferenceAddForm, VideoConferenceChangeForm

# Register your models here.


class VideoConferenceAdmin(admin.ModelAdmin):
  add_form = VideoConferenceAddForm 
  form = VideoConferenceChangeForm
  model = VideoConference
  list_display = ['title', 'host', 'start_time', 'end_time', 'created_at', 'updated_at']


admin.site.register(VideoConference, VideoConferenceAdmin)


