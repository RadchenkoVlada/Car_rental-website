from django.urls import path
from . import views
# Serving files uploaded by a user during development
from django.conf import settings
from django.conf.urls.static import static

app_name = "rentalcar"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
