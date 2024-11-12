from django import forms
from .models import UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','email','password1','password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['email','password']
