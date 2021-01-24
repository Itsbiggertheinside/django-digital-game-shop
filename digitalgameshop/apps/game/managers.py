from django.db import models
from .helpers import StatusChoice


class GameQuerySet(models.QuerySet):

    # def top_rated_games(self, size):
    #     calculate_rating = 
    #     return self.aggregate(models.Max(calculate_rating))[:size]

    def latest_released_games(self, size):
        return self.filter(status=StatusChoice.ON_SALE).order_by('-release_date')[:size]

    def pre_ordered_games(self, size):
        return self.filter(status=StatusChoice.PRE_ORDER).order_by('-release_date')[:size]

    def favourited_games(self, id):
        return self.filter(favourites__id=id)

    def comments(self, id):
        return self.filter(parent__id=id)


class GameManager(models.Manager):
    def get_queryset(self):
        return GameQuerySet(self.model, using=self._db)

    # def get_top_rated_games(self, size):
    #     return self.get_queryset().top_rated_games(size)

    def get_latest_released_games(self, size):
        return self.get_queryset().latest_released_games(size)

    def get_pre_ordered_games(self, size):
        return self.get_queryset().pre_ordered_games(size)

    def get_favourited_games(self, id):
        return self.get_queryset().favourited_games(id)


# class RatingManager(models.Manager):
#     def get_queryset(self):
#         return GameQuerySet(self.model, using=self._db)

#     def get_ratings(self, id):
#         return self.get_queryset().ratings(id)
    

class CommentManager(models.Manager):
    def get_queryset(self):
        return GameQuerySet(self.model, using=self._db)

    def get_comments(self, id):
        return self.get_queryset().comments(id)