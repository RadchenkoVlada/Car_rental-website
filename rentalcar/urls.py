from django.urls import path
from . import views

app_name = "rentalcar"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),

]
