from django.shortcuts import render
from django.views.generic import ListView
from .models import Game
from .helpers import GameListHelper

# Create your views here.
class HomeView(ListView):
    game_lister = GameListHelper()
    queryset = game_lister.queryset
    template_name = 'base/home.html'

        
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['top_games'] = self.game_lister.get_top_games()
        context['latest_released_games'] = self.game_lister.get_latest_released_games()
        context['pre_ordered_games'] = self.game_lister.get_pre_ordered_games()
        return context
    