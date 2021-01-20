from uuid import uuid4


class GameListViewHelper():

    def __init__(self, model):
        self.queryset = model.objects.select_related('user').prefetch_related('genres', 'languages', 'platform').all()

    def get_top_games(self):
        pass
    def get_latest_released_games(self):
        return self.queryset.filter(pre_order=False).order_by('-release_date')[:10]
    def get_pre_ordered_games(self):
        return self.queryset.filter(pre_order=True).order_by('-release_date')[:10]

class MediaDirectory():

    def upload_media(self, instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.game.user.id, file_name)

    def upload_banner(self, instance, filename):
        file_format = filename.split('.')[-1] # .jpg, .png
        file_name = f'{str(uuid4())}.{file_format}'
        return 'uploads/user_{0}/games/{1}'.format(instance.user.id, file_name)