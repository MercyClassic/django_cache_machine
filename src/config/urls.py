from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config.settings import DEBUG, MEDIA_ROOT, MEDIA_URL, STATIC_ROOT, STATIC_URL

from .swagger import urlpatterns as doc_urls

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('core.urls')),
] + doc_urls


if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
