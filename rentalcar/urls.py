from django.urls import path
from . import views


app_name = "rentalcar"

urlpatterns = [
	path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('user_registration/', views.user_registration, name='user_registration')
]