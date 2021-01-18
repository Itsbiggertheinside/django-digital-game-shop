from django.db import models
from .game_dependencies import Genre, Language, Platform
from .ratings import GameRatings


class Game(models.Model):

    user = models.ForeignKey('user.Account', on_delete=models.CASCADE, related_name='oyunlar')

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)

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


    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if not :
    #         rating = GameRatings(game=self.pk, likes=0, comments=0, wisheds=0)
    #         rating.save()
    #         super(Game, self).save(*args, **kwargs)
        
    #     super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Oyun'
        verbose_name_plural = 'Oyunlar'