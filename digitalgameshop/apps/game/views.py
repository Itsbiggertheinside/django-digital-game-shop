from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Game, GameImage
from user.models.profile import Account
from django.http import HttpResponseRedirect



#-----------------------------------------------------------------------------------------------------------------
class QueryHelper():
    queryset = Game.objects.select_related('user').prefetch_related('genres', 'languages', 'platform', 'favourites')
    def get_top_games(self):
        pass
    def get_latest_released_games(self):
        return self.queryset.filter(pre_order=False).order_by('-release_date')[:10]
    def get_pre_ordered_games(self):
        return self.queryset.filter(pre_order=True).order_by('-release_date')[:10]
#-----------------------------------------------------------------------------------------------------------------



# Create your views here.
class GameHomeView(ListView):
    queryset = QueryHelper()
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
    template_name = 'base/favourites.html'
    context_object_name = 'game_favourites'

    def get_queryset(self):
        queryset = QueryHelper().queryset
        favourited_games_by_user = queryset.filter(favourites__id=self.request.user.id)
        return favourited_games_by_user


@login_required
def add_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.add(request.user.id)
    return HttpResponseRedirect(game.get_absolute_url())

@login_required
def remove_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.remove(request.user.id)
    return redirect('game:favourites')

@login_required
def add_checkout(request, slug):
    pass

@login_required
def remove_checkout(request, slug):
    pass