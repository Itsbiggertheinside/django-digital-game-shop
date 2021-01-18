from django.db import models
from . import Genre, Language, Platform


class Game(models.Model):

    user = models.ForeignKey('user.Account', on_delete=models.CASCADE, related_name='oyunlar')

    name = models.CharField(max_length=35)
    price = models.PositiveSmallIntegerField()
    developer = models.CharField(max_length=55)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)

    requirements_minimum = models.TextField(null=True, blank=True)
    requirements_recommended = models.TextField(null=True, blank=True)

    on_sale = models.BooleanField(default=True)
    pre_order = models.BooleanField(default=False)
    stock = models.PositiveIntegerField()

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