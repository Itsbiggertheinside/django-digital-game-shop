from django.db import models
from django.contrib.auth.models import User
from .helpers import upload_media


#------------------------------------------------------
# MANY TO MANY - GAME RELATIONS                         |
#------------------------------------------------------

class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

#-------------------------------------------------------


class GameImage(models.Model):
    game = models.ForeignKey('store.Game', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_media)


class Comment(models.Model):
    parent = models.ForeignKey('store.Game', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.owner.username} - {self.parent.name}'
