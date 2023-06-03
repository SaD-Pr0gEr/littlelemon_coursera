from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurant.urls')),
    path('api/', include('restaurant_api.urls')),
    path('auth/', include('djoser.urls')),
    path('api-token-auth/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
