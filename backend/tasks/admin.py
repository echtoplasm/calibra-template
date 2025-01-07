from django.contrib import admin
from .forms import TaskForm, TaskChangeForm
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    form = TaskForm
    add_form = TaskChangeForm
    list_display = ['task_name', 'task_owner', 'task_assigned_to']
    search_fields = ['task_name', 'task_owner', 'task_assigned_to']
    list_filter = ['task_owner', 'task_assigned_to']

admin.site.register(Task, TaskAdmin)
