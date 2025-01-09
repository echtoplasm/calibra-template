from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.contrib.auth import views as auth_views


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
    path('api/', include('api.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
