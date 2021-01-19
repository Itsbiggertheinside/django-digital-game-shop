from .models import Game, GameRatings


class GameListHelper():
    
    queryset = Game.objects.select_related('user').prefetch_related('genres', 'languages', 'platform').all()

    def get_top_games(self):
        pass
    def get_latest_released_games(self):
        return self.queryset.filter(pre_order=False).order_by('-release_date')[:10]
    def get_pre_ordered_games(self):
        return self.queryset.filter(pre_order=True).order_by('-release_date')[:10]
