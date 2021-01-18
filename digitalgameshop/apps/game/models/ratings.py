from django.db import models

class GameRatings(models.Model):
    game = models.OneToOneField('game.Game', on_delete=models.CASCADE, primary_key=True, related_name='ratings')
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveSmallIntegerField(default=0)
    wisheds = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.game