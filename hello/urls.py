from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from landings import views as landings

urlpatterns = [
    path('', landings.index, name='landing'),
    path('cv/', landings.cv, name='cv'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
