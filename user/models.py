from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField('핸드폰번호', max_length=20)
    address = models.TextField(max_length=200)
