from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=15)
    adresse = models.TextField()

