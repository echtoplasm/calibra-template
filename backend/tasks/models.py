from django.db import models
from django.conf import settings

# Create your models here.

CustomUser = settings.AUTH_USER_MODEL

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    task_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_assigned_to')
    task_due_date = models.DateTimeField()
    task_priority = models.CharField(max_length=255)
    task_status = models.CharField(max_length=255)
    task_comments = models.TextField()

