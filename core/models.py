from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    
    
class About(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="about_img") 
    
    

class CreativeTeams(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to= "about_img" )
