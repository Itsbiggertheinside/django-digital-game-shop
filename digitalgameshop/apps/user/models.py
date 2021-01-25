from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import upload_media



# Create your models here.
class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to=upload_media, default='default-profile-pic.jpg')
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    slug = models.SlugField(primary_key=True)

    
    def save(self, *args, **kwargs):
        self.slug = self.username
        super(Account, self).save(*args, **kwargs)

    def __str__(self):
        return self.username