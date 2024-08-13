from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    photo_profil = models.ImageField(blank=True, null=True, upload_to='user_profil')
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    email = models.EmailField(unique=True)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]