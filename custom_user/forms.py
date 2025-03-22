# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # Renombrar el campo

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name")