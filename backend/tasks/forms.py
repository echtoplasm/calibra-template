from django import forms 
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['task_name', 'task_description', 'task_owner', 'task_assigned_to', 'task_due_date', 'task_priority', 'task_status', 'task_comments']

class TaskChangeForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['task_name', 'task_description', 'task_owner', 'task_assigned_to', 'task_due_date', 'task_priority', 'task_status', 'task_comments']


