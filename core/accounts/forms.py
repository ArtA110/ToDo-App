from django.forms import ModelForm
from .models import User, Profile
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email','password1','password2']