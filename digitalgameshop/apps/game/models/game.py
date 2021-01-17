from django.db import models
from apps.game.models.game_dependencies import Genres, Languages, Platform

class Game(models.Model):

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()

    requirements_minimum = models.TextField()
    requirements_recommended = models.TextField()

    # dependencies
    genres = models.ManyToManyField(Genres)
    languages = models.ManyToManyField(Languages)
    platform = models.ManyToManyField(Platform)


    def __str__(self):
        return self.name
