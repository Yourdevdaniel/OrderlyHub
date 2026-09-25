from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
import uuid
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email_verified = models.BooleanField(default=False)
    
    REQUIRED_FIELDS = ["email", "username"]
    
    class Meta:
        verbose_name = 'User'
        
    def __str__(self) -> str:
        return self.username

class SocialAccount(models.Model):
    PROVIDERS =(
        ("google","Google"),
        ("github","Github"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_accounts')
    provider = models.CharField(max_length=20, choices=PROVIDERS)
    provider_uid = models.CharField(max_length=125)
    extra_data = models.JSONField(default=dict, blank=True)
    
    class Meta:
        # Ensures that a user can only have one Google account, or one GitHub account.
        unique_together = ("provider","provider_uid")
        
class EmailVerificationToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email')
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    is_used = models.BooleanField(default=False)
    
8