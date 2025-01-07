from django.contrib import admin
from .models import Notification
from .forms import NotificationForm, NotificationChangeForm
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    form = NotificationForm
    add_form = NotificationChangeForm
    list_display = [
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

admin.site.register(Notification, NotificationAdmin)
