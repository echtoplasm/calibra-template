from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConferenceList.as_view(), name='conference_list'),
    path('<int:pk>/', views.ConferenceDetail.as_view(), name='conference_detail'),
]
