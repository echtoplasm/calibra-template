from django.db import models
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class VideoConference(models.Model):
    title = models.CharField(max_length=100)
    host = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='host', 
        help_text='The user who created the conference'
    )
    description = models.TextField(blank=True, help_text='A brief description of the conference')
    start_time = models.DateTimeField(default=now)
    end_time = models.DateTimeField(default=now() + timedelta(hours=1))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='participants',
        blank=True
    )

    def __str__(self):
        number_of_participants = self.participants.count()
        return f"{self.title} ({number_of_participants} participants)"
