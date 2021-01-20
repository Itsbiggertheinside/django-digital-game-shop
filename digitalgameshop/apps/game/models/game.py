from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from uuid import uuid4
from .game_dependencies import Genre, Language, Platform
from .upload_to import MediaDirectory

class Game(models.Model):
    md = MediaDirectory()

    user = models.ForeignKey('user.Account', on_delete=models.CASCADE, related_name='oyunlar')

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)

    banner = models.ImageField(upload_to=md.upload_banner)
    requirements_minimum = models.TextField(null=True, blank=True)
    requirements_recommended = models.TextField(null=True, blank=True)

    on_sale = models.BooleanField(default=True)
    pre_order = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()

    # dependencies
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    platform = models.ManyToManyField(Platform)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.name

    def get_platforms(self):
        platform_set = self.platform.all()
        platforms = [platform.name for platform in platform_set]
        return platforms

    def get_absolute_url(self):
        return reverse('game:detail', kwargs={'slug': self.slug})

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