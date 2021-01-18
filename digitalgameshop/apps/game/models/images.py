from django.db import models
from . import Game
from uuid import uuid4


def upload_media(instance, filename):
    file_format = filename.split('.')[-1] # .jpg, .png
    file_name = f'{str(uuid4())}.{file_format}'
    return 'uploads/user_{0}/games/{1}'.format(instance.game.user.id, file_name)

class GameImage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_media)

    