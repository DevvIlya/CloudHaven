from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from myapp.views import custom_register, csrf_token_view

from myapp.views import UserViewSet, StorageFilesViewSet
from myapp.views import index


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
router.register(r'storagefiles', StorageFilesViewSet)

urlpatterns = [
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
