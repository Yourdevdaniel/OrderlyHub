from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username:str, email:str, password: str = None, **extra_fields) -> "User":
        if not username:
            raise ValueError('O campo "Username" não pode ser inválido')
        if not email:
            raise ValueError('O campo "Email" não pode ser inválido')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'User'
        
    def __str__(self) -> str:
        return self.username
