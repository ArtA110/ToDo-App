from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_("EMAIL MUST SET!"))
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff',True)

        if kwargs.get('is_staff') is not True:
            raise ValueError(_("superuser must have is_staff = True"))
        
        return self.create_user(email,password,**kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique= True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    object = UserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.first_name+' '+self.last_name
