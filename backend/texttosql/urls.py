from .views import text_to_sql
from django.urls import path

urlpatterns = [
    path('', text_to_sql),
]
