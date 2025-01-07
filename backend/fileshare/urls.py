from django.urls import path
from . import views

urlpatterns = [
    path('files/', views.FileList.as_view(), name='file_list'),
    path('files/<int:pk>/', views.FileDetail.as_view(), name='file_detail'),
    path('file_access/', views.FileAccessList.as_view(), name='file_access_list'),
    path('file_access/<int:pk>/', views.FileAccessDetail.as_view(), name='folder_access_detail'),
]
