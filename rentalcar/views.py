from django.shortcuts import render, redirect

# Create your views here.
from rentalcar.forms import RegisterForm

from django.urls import reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm



def homepage(request):
    return render(request,
            template_name='rentalcar/home.html')

def about(request):
    return render(request,
            template_name='rentalcar/about.html')




def user_registration(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            #validating the password match while creating the user.
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            raw_pass = form.cleaned_data.get('password')
            login(request,user)
            # redirect to a new URL:
            return redirect("rentalcar:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: form.error_messages[msg]")
            return render(request = request,
                          template_name = "rentalcar/user_registration.html",
                          context = {"form":form})

    form = RegisterForm()
    return render(request = request,
                          template_name = "rentalcar/user_registration.html",
                          context = {"form":form})




def logout_request(request):
    logout(request)
    messages.info(request, "Logget out successfully!")
    return redirect("rentalcar:homepage")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("rentalcar:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    

    form = AuthenticationForm()
    return render(request,
                  "rentalcar/login.html",
                  {"form":form})






