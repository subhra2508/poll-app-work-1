from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class profileUpdateForm(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=['user']