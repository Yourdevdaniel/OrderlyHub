from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User'
        
    def __str__(self) -> str:
        return self.username
