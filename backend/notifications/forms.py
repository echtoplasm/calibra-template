from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = [
            'notification_title', 
            'notification_message', 
            'notification_date', 
            'notification_time', 
            'notification_sender', 
            'notification_receiver', 
            'notification_status', 
            'notification_read', 
            'notification_deleted', 
            'notification_archived', 
            'notification_priority', 
            'notification_url', 
            'notification_image', 
            'notification_attachment', 
        ]

class NotificationChangeForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = [
            'notification_title', 
            'notification_message', 
            'notification_date', 
            'notification_time', 
            'notification_sender', 
            'notification_receiver', 
            'notification_status', 
            'notification_read', 
            'notification_deleted', 
            'notification_archived', 
            'notification_priority', 
            'notification_url', 
            'notification_image', 
            'notification_attachment', 
        ]
