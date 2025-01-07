from django.db import models
from django.conf import settings

CustomUser = settings.AUTH_USER_MODEL

# Create your models here.

class File(models.Model):
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uploaded_by')

class FileAccess(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_share = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

def __str__(self):
  return self.file_name
