from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from manual.views import main_page
from .yasg import urlpatterns as swagger_urls

urlpatterns = [
    path("", main_page, name="main"),
    path('admin/', admin.site.urls),
    path('api/v1/', include('manual.api.v1.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += swagger_urls


admin.site.site_header = "КОМТЕК"
admin.site.site_title = "Админ панель - КОМТЕК"
admin.site.index_title = "Добро пожаловать в КОМТЕК"
