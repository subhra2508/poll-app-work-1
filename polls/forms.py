from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment

class createNewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['content','catagory']
class giveCommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['body']
        