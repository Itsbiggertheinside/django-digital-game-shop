from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, GameImage


class GameListViewHelper():

    queryset = Game.objects.select_related('user').prefetch_related('genres', 'languages', 'platform').all()

    def get_top_games(self):
        pass

    def get_latest_released_games(self):
        return self.queryset.filter(pre_order=False).order_by('-release_date')[:10]

    def get_pre_ordered_games(self):
        return self.queryset.filter(pre_order=True).order_by('-release_date')[:10]


# Create your views here.
class GameHomeView(ListView):
    queryset = GameListViewHelper()
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super(GameHomeView, self).get_context_data(**kwargs)
        # context['games'] = self.queryset
        # context['top_games'] = self.queryset.get_top_games()
        context['latest_released_games'] = self.queryset.get_latest_released_games()
        context['pre_ordered_games'] = self.queryset.get_pre_ordered_games()
        return context
    
class GameDetailView(DetailView):
    model = Game
    template_name = 'base/detail.html'
    context_object_name = 'game_detail'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context['images'] = GameImage.objects.select_related('game').filter(game=self.get_object())
        return context

class GameFavoritesView(LoginRequiredMixin, ListView):
    model = Game
    template_name = 'base/favorites.html'