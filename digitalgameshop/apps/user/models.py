from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import upload_media



# Create your models here.
class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to=upload_media, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)


    def __str__(self):
        return self.username



class CheckOut(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    item = models.ManyToManyField('game.Game', related_name='checkout_item', blank=True)

    def __str__(self):
        return f'{self.user.username}\'s checkout list'
