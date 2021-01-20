from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class GameRatings(models.Model):
    game = models.OneToOneField('game.Game', on_delete=models.CASCADE, primary_key=True, related_name='ratings')
    likes = models.JSONField(default=dict)
    comments = models.JSONField(default=dict)
    favorites = models.JSONField(default=dict)

    def __str__(self):
        return str(self.game)

    def get_like_count(self):
        pass
    def get_comment_count(self):
        pass
    def get_favorite_count(self):
        pass