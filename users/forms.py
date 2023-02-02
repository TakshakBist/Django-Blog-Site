"""
    I need an email field in my default django form so Iam making one

    Class Meta: Model Meta is basically the inner class of your model class. Model Meta is basically used to change the
    behavior of your model fields like changing order options,verbose_name, and a lot of other options. It’s completely
    optional to add a Meta class to your model.

"""

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
