from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from .helpers import upload_media



# Create your models here.
class Account(AbstractUser):
    profile_pic = models.ImageField(upload_to=upload_media, default='default-profile-pic.jpg')
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    slug = models.SlugField(primary_key=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self, **kwargs):
        return reverse('profile', kwargs={'slug': self.slug})
    
    def get_checkout_url(self, **kwargs):
        return reverse('checkout', kwargs={'slug': self.slug})

    def add_item_to_checkout_url(self, **kwargs):
        return reverse('add-checkout', kwargs={'slug': self.slug})
    
    def remove_item_from_checkout_url(self, **kwargs):
        return reverse('remove-checkout', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username.replace('ı', 'i'))
            return super(Account, self).save(*args, **kwargs)
        super().save(*args, **kwargs)


class CheckoutItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='checkouts', related_query_name='checkout')
    reference = models.ManyToManyField('game.Game', related_name='checkouts', related_query_name='checkout')

    def __str__(self):
        return '{0}\'s Checkout List'.format(self.owner.username)