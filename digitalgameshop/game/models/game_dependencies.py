from django.db import models


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