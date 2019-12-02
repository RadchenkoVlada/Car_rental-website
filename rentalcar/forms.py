from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=False, label='Your e-mail address')
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "Last name")
    
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
