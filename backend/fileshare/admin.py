from django.contrib import admin
from .models import File, FileAccess
from .forms import FileForm, FileAccessForm
# Register your models here.


class FileAdmin(admin.ModelAdmin):
    form = FileForm
    add_form = FileAccessForm
    list_display = ['file_name', 'owner', 'uploaded_by']
    search_fields = ['file_name', 'owner', 'uploaded_by']
    list_filter = ['owner', 'uploaded_by']

admin.site.register(File, FileAdmin)
