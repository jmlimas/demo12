
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.principal.urls')), 
    path('', include('apps.users.urls',namespace='users_app')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


 
   