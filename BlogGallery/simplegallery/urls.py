from django.urls import path
from . import views
from django.conf.urls.static import static
from BlogGallery import settings

urlpatterns = [
                  path('auth/', views.auth),
                  # path('auth/', views.get_gallery),
                  path('form/', views.get_form),
                  path('main_page/<int:user>/', views.main_page),
                  path('', views.main_page),
                  path('get_theme/<str:theme>/', views.get_theme)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
