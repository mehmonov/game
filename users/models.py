from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

import datetime
class UserProfile(AbstractUser):
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=50,  unique=True)
    age = models.CharField(max_length=3, blank=True)
    phone_number = models.CharField(max_length=25)
    activate_user = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"User - {self.full_name}"


