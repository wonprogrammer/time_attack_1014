from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings

# Create your models here.

class User(AbstractUser):
    profile = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
