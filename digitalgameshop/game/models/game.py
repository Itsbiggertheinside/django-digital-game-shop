from django.db import models
from game.models.game_dependencies import *

class Game(models.Model):

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()

    requirements_minimum = models.TextField()
    requirements_recommended = models.TextField()

    # dependencies
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    platform = models.ManyToManyField(Platform)


    def __str__(self):
        return self.name
