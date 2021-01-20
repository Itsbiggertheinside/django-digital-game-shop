from django.shortcuts import render
from django.views.generic import ListView
from .models import Game, GameImage
from .models.helpers import GameListViewHelper

# Create your views here.
class HomeView(ListView):
    model = Game
    queryset = GameListViewHelper(model)
    template_name = 'base/home.html'

        
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context['games'] = self.queryset
        # context['top_games'] = self.queryset.get_top_games()
        context['latest_released_games'] = self.queryset.get_latest_released_games()
        context['pre_ordered_games'] = self.queryset.get_pre_ordered_games()
        return context
    