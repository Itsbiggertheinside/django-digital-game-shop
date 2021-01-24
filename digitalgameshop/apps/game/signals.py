# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Game, GameRatings

# @receiver(post_save, sender=Game)
# def create_ratings(sender, instance, created, **kwargs):
#     if created:
#         GameRatings.objects.create(game=instance)

# @receiver(post_save, sender=Game)
# def update_ratings(sender, instance, created, **kwargs):
#     if created == False:
#         instance.ratings.save()