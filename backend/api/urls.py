from django.urls import path

from tasks.views import TaskListCreate, TaskDetail, TaskToggleComplete

from notifications.views import NotificationList, NotificationDetail

from messenger.views import ConversationList, ConversationDetail, MessageList, MessageDetail

from conference.views import ConferenceList, ConferenceDetail

from fileshare.views import FileList, FileDetail, FileAccessList, FileAccessDetail

from texttosql.views import text_to_sql

from . import views


urlpatterns = [

    #tasks urls#
    path('tasks/', TaskListCreate.as_view()),
    path('tasks/<int:pk>/', TaskDetail.as_view()),
    path('tasks/<int:pk>/complete/', TaskToggleComplete.as_view()),
    

    #notifications urls#
    path('notifications/', NotificationList.as_view()),
    path('notifications/<int:pk>/', NotificationDetail.as_view()),

    #messenger urls#
    path('messenger/conversations/', ConversationList.as_view()),
    path('messenger/conversations/<int:pk>/', ConversationDetail.as_view()),
    path('messenger/messages/', MessageList.as_view()),
    path('messenger/messages/<int:pk>/', MessageDetail.as_view()),

    #conference urls#
    path('conferences/', ConferenceList.as_view()),
    path('conferences/<int:pk>/', ConferenceDetail.as_view()),

    #fileshare urls#
    path('fileshare/files/', FileList.as_view()),
    path('fileshare/files/<int:pk>/', FileDetail.as_view()),
    path('fileshare/access/', FileAccessList.as_view()),
    path('fileshare/access/<int:pk>/', FileAccessDetail.as_view()),

    #texttosql urls#
    path('v1/texttosql/convert/', text_to_sql, name='text-to-sql'),

    #auth urls#
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]

