from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Game, GameImage
from .models.helpers import GameListViewHelper

# Create your views here.
class GameHomeView(ListView):
    queryset = GameListViewHelper(Game)
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