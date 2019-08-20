from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('apps.blog.urls')),
    #path('admin/', include('trexsite.hostsconf.admin_urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.trexapp.views.error_404_view'
handler403 = 'apps.trexapp.views.error_403_view'