from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from accounts.views import signup, login_view

def api_overview(request):
    return JsonResponse({
        'Tasks': '/api/tasks/v1/',
        'Notifications': '/api/notifications/v1/',
        'Messenger': '/api/messenger/v1/',
        'Conferences': '/api/conferences/v1/',
        'Fileshare': '/api/fileshare/v1/',
        'Text-to-SQL': '/api/v1/texttosql/convert/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/v1/', include('tasks.urls')),
    path('api/notifications/v1/', include('notifications.urls')),
    path('api/messenger/v1/', include('messenger.urls')),
    path('api/conferences/v1/', include('conference.urls')),
    path('api/fileshare/v1/', include('fileshare.urls')),
    path('api/texttosql/v1/', include('texttosql.urls')),  
    path('api/', api_overview),
    path('login/', login_view),
    path('signup/', signup),
]
