from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from uuid import uuid4
from django.conf import settings
from .dependencies import Genre, Language, Platform
from .managers import GameManager, CommentManager
from .helpers import upload_media, upload_banner


class Game(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='games', related_query_name='game_qs')

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)

    banner = models.ImageField(upload_to=upload_banner)
    requirements_minimum = models.TextField(null=True, blank=True)
    requirements_recommended = models.TextField(null=True, blank=True)

    on_sale = models.BooleanField(default=True)
    pre_order = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()

    # dependencies
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    platform = models.ManyToManyField(Platform)

    # special
    favourites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favourites', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True)

    manager = GameManager()


    def __str__(self):
        return self.name

    def get_platforms(self):
        platform_set = self.platform.all()
        platforms = [platform.name for platform in platform_set]
        return platforms

    def get_absolute_url(self):
        return reverse('game:detail', kwargs={'slug': self.slug})

    def add_favourite_url(self):
        return reverse('game:add-favourite', kwargs={'slug': self.slug})
    
    def remove_favourite_url(self):
        return reverse('game:remove-favourite', kwargs={'slug': self.slug})

    def create_unique_slug(self):
        letter_fix = slugify(self.name.replace('ı', 'i'))
        random_char = uuid4().hex[:4]
        url = f'{letter_fix}-{random_char}'
        return url        
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.create_unique_slug()
            return super(Game, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_at']


class GameImage(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_media)




class GameRatings(models.Model):
    game = models.OneToOneField('game.Game', on_delete=models.CASCADE, primary_key=True, related_name='ratings')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='game_likes', blank=True)
    comments = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='game_comments', blank=True)
    favourites = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='game_favourites', blank=True)

    def __str__(self):
        return str(self.game)

    def get_like_count(self):
        return self.likes.count()
    def get_comment_count(self):
        return self.comments.count()
    def get_favourite_count(self):
        return self.favourites.count()

    def calculate_score(self):
        score = (1 + self.get_like_count()) * (1 + self.get_comment_count / 3) * (1 + self.get_favourite_count * 2)
        return score


class Comment(models.Model):
    parent = models.ForeignKey(Game, on_delete=models.PROTECT, related_name='game_comments')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.parent.name}'

    manager = CommentManager()
