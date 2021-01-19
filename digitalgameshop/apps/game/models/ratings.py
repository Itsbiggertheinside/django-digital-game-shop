from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .game import Game

class GameRatings(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True, related_name='ratings')
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveSmallIntegerField(default=0)
    wisheds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.game)
