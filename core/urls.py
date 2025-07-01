from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf.urls.static import static

from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #apis
    path('api/v1/auth/', include("apps.users.auth.urls")),

]

urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
