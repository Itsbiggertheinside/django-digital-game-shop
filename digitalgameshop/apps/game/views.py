from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Game, GameImage
from django.http import HttpResponse



# Create your views here.
class GameHomeView(ListView):
    model = Game
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super(GameHomeView, self).get_context_data(**kwargs)
        context['latest_released_games'] = self.model.manager.get_latest_released_games(10)
        context['pre_ordered_games'] = self.model.manager.get_pre_ordered_games(10)
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
    template_name = 'base/favourites.html'
    context_object_name = 'game_favourites'

    def get_queryset(self):
        return Game.manager.get_favourited_games(self.request.user.id)
    


@login_required
def add_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.add(request.user.id)
    return HttpResponse('added')

@login_required
def remove_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.remove(request.user.id)
    return HttpResponse('removed')

@login_required
def add_checkout(request, slug):
    pass

@login_required
def remove_checkout(request, slug):
    pass