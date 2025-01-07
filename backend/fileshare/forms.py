from django import forms
from .models import File, FileAccess

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_name', 'file', 'description', 'owner', 'uploaded_by']

class FileAccessForm(forms.ModelForm):
    class Meta:
        model = FileAccess
        fields = ['file', 'user', 'can_view', 'can_edit', 'can_share', 'can_delete']
