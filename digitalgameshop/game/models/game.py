from django.db import models
from game.models.game_dependencies import Genre, Language, Platform


class Game(models.Model):

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()
    release_date = models.DateField(null=True)

    requirements_minimum = models.TextField()
    requirements_recommended = models.TextField()

    on_sale = models.BooleanField(default=True)
    pre_order = models.BooleanField(default=False)

    # dependencies
    genres = models.ManyToManyField(Genre)
    languages = models.ManyToManyField(Language)
    platform = models.ManyToManyField(Platform)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Oyun'
        verbose_name_plural = 'Oyunlar'