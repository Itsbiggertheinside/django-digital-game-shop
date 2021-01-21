from django.db import models
from .profile import Account


class CheckOut(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    item = models.ManyToManyField('game.Game', related_name='checkout_item', blank=True)

    def __str__(self):
        return f'{self.user.username}\'s checkout list'