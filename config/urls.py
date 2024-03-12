
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger_conf import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("users.urls")),
    path('main/', include('main.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
