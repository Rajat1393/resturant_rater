from dataclasses import field
from distutils.errors import LinkError
from turtle import title
from django import forms, views
from django.contrib.auth.models import User
from rater.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta: 
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm): 
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

