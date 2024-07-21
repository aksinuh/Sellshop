from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    photo_profil = models.ImageField(blank=True, null=True, upload_to='user_profil')
    first_name = models.CharField(max_length=100, blank=True)