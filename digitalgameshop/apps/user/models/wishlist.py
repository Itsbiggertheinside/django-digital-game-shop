from django.db import models
from .profile import Account


class CheckOut(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    item = models.PositiveIntegerField()

    def __str__(self):
        return self.user