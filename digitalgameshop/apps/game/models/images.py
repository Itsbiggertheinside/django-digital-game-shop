from django.db import models
from .helpers import MediaDirectory

class GameImage(models.Model):
    md = MediaDirectory()

    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=md.upload_media)

    