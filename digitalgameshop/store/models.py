from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.shortcuts import reverse
from django.utils.text import slugify
from .submodels import Genre, Language, Platform
from .helpers import upload_media, STATUS_CHOICE

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=35)
    developer = models.CharField(max_length=55)
    description = models.TextField()
    price = models.FloatField()
    release_date = models.DateField(null=True, blank=True)
    metascore = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    
    requirements_minimum = models.TextField(null=True, blank=True)
    requirements_recommended = models.TextField(null=True, blank=True)

    stock = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='ON_SALE')
    banner = models.ImageField(upload_to=upload_media)

    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    platforms = models.ManyToManyField(Platform)

    favourites = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    @property
    def get_platforms(self):
        return [platform.name for platform in self.platforms.all()]

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})

    def add_favourite_url(self):
        return reverse('add-favourite', kwargs={'id': self.id})
    
    def remove_favourite_url(self):
        return reverse('remove-favourite', kwargs={'id': self.id})

    def add_to_order_url(self):
        return reverse('add-to-order', kwargs={'id': self.id})

    def create_unique_slug(self):
        letter_fix = slugify(self.name.replace('ı', 'i'))
        random_char = uuid4().hex[:4]
        url = f'{letter_fix}-{random_char}'
        return url        
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_unique_slug()
            return super(Game, self).save(*args, **kwargs)
        
        super().save(*args, **kwargs)


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.owner}\'ın Sepeti'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Game, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.order.owner}\'a ait {self.item.name} isimli oyundan {self.quantity} adet'

    def plus_quantity_url(self):
        return reverse('plus-quantity', kwargs={'id': self.id})

    def less_quantity_url(self):
        return reverse('less-quantity', kwargs={'id': self.id})

    def remove_from_order_url(self):
        return reverse('remove-item', kwargs={'id': self.id})