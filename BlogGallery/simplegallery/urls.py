from django.urls import path
from . import views
from django.conf.urls.static import static
from BlogGallery import settings

urlpatterns = [
    path("", views.get_gallery),
    path("form/", views.get_form)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)