from django.db import models
from .profile import Account

class Favourite(models.Model):
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='favourites')

    def __str__(self):
        return self.game

class CheckOut(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    item = models.PositiveIntegerField()

    def __str__(self):
        return self.user