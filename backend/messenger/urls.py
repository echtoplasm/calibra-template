from django.urls import path
from . import views

urlpatterns = [
    path('conversations/', views.ConversationList.as_view(), name='Conversation_list'),
    path('conversations/<int:pk>/', views.ConversationDetail.as_view(), name='Conversation_detail'),
    path('messages/', views.MessageList.as_view(), name='Message_list'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='Message_detail'),
]


