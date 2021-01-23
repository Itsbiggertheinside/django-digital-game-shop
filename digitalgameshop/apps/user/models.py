from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import upload_media



# Create your models here.
class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to=upload_media, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.username