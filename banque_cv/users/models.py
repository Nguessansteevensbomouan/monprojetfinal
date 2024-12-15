from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    email = models.EmailField(unique=True)
    tel = models.CharField(max_length=15)
    adresse = models.TextField()
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set')
