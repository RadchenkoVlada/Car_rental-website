from django.urls import path
from . import views


app_name = "rentalcar"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
]