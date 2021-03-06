
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('file/', include('file_upload.urls')),
    path('account/', include('file_upload.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
