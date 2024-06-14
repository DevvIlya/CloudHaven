from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from myapp.views import custom_register, csrf_token_view

from myapp.views import UserViewSet, StorageFilesViewSet
from myapp.views import index
from django.views.generic import TemplateView
from django.urls import path
from myapp import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'storagefiles', StorageFilesViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('', index, name='index'),
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/register/', custom_register, name='custom_register'),

    # эндпоинт для получения токенов
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/csrf/', csrf_token_view, name='api-csrf'),

    path('storagefiles/by_user/', StorageFilesViewSet.as_view({'get': 'by_user'}), name='storagefiles-by-user'),
    path('storagefiles/<int:pk>/generate_short_link/', StorageFilesViewSet.as_view({'post': 'generate_short_link'}),
         name='storagefiles-generate-short-link'),

    path('admin/', views.admin_page, name='admin_page'),
    path('file/', views.file_page, name='file_page'),
    path('', views.main_page, name='main_page'),
    path('not-found/', views.not_found_page, name='not_found_page'),
    path('storage/', views.storage_page, name='storage_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
