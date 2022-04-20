from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    is_host = models.BooleanField('Is Host', default=False)
    is_attendee = models.BooleanField('Is Attendee', default=False)
    
    
class Event(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)
    description = models.TextField()
    drinks = models.CharField(max_length=100)
    games = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    image = CloudinaryField('image', null=True,blank=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.username