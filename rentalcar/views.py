from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
	return render(request,
 			template_name='rentalcar/home.html',
 			context={"tutorials": Tutorial.objects.all})

def user_registration(request):
 	form = UserCreationForm
 	return render(request=request,
 				template_name='rentalcar/user_registration.html', 
 				context={"form":form})
