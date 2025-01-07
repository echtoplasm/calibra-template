from django.db import models
import datetime
from django.conf import settings
# Create your models here.

CustomUser = settings.AUTH_USER_MODEL

class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('invitation', 'Invitation'),
        ('reminder', 'Reminder'),
        ('alert', 'Alert'),
        ('warning', 'Warning'),
        ('information', 'Information'),
    )
    notification_id = models.AutoField(primary_key=True)
    notification_title = models.CharField(max_length=100)
    notification_message = models.CharField(max_length=100)
    notification_date = models.DateField()
    notification_time = models.TimeField()
    notification_sender = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='notification_sender'
    )
    notification_receiver = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='notification_receiver'
    )
    notification_status = models.CharField(max_length=100)
    notification_read = models.BooleanField()
    notification_deleted = models.BooleanField(default=False)
    notification_archived = models.BooleanField(default=False)  
    notification_priority = models.IntegerField(default=False)
    notification_url = models.CharField(max_length=100)
    notification_image = models.ImageField(upload_to='images/', blank=True, null=True)
    notification_attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.notification_title
