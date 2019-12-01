from django.shortcuts import render, redirect

# Create your views here.
from rentalcar.forms import RegisterForm

from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def homepage(request):
	return render(request,
		    template_name='rentalcar/home.html')

def user_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
    	# create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
        	user = form.save()
        	login(request, user)
        	# redirect to a new URL:
        	return redirect("rentalcar:homepage")
       	else:
            for msg in form.error_messages:
	            messages.error(request, f"{msg}: form.error_messages[msg]")

    form = RegisterForm
    return render(request=request, 
    	template_name='rentalcar/user_registration.html', 
    	context={"form":form})