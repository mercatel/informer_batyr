from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from informer_batyr import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('batyr.urls')),
                  path("ckeditor/", include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
