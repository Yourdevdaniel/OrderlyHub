from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, null=False, unique=True)
    email = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User'
        
    def __str__(self) -> str:
        return self.username
    