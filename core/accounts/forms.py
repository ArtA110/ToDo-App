from django.forms import ModelForm
from .models import User, Profile
from django.utils.translation import gettext_lazy as _
# from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password']
