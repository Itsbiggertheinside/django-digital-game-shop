from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Min, Max, F, Q, PositiveIntegerField, ExpressionWrapper
from .models import Game, GameImage, Comment
from .forms import CommentForm
from user.models import CheckoutItem



# Create your views here.
class GameHomeView(ListView):
    model = Game
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        
        get_top_rated_games = Game.objects.select_related('user') \
        .prefetch_related('genres', 'languages', 'platform').annotate(
            scores=ExpressionWrapper((F('metascore') * ( 1 + F('favourites'))), 
            output_field=PositiveIntegerField())) \
            .order_by('-scores')

        get_latest_released_games = Game.objects.select_related('user') \
        .prefetch_related('platform').filter(status='ON_SALE').order_by('-release_date')

        get_pre_ordered_games = Game.objects.select_related('user') \
        .prefetch_related('platform').filter(status='PRE_ORDER').order_by('-release_date')

        context = super(GameHomeView, self).get_context_data(**kwargs)
        context['top_rated_games'] = get_top_rated_games[:5]
        context['latest_released_games'] = get_latest_released_games[:10]
        context['pre_ordered_games'] = get_pre_ordered_games[:10]
        return context
    

class GameDetailView(DetailView):
    model = Game
    template_name = 'base/detail.html'
    context_object_name = 'game_detail'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)
        context['images'] = GameImage.objects.select_related('game').filter(game=self.get_object())
        context['comments'] = Comment.objects.select_related('parent', 'owner').filter(parent__id=self.get_object().id)
        context['comment_form'] = CommentForm
        context['latest_released_games'] = Game.objects.filter(status='ON_SALE').order_by('-release_date')[:10]
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)
        if form.is_valid():
            parent = self.get_object()
            owner = request.user
            comment = form.cleaned_data.get('comment')
            send = Comment(parent=parent, owner=owner, comment=comment)
            send.save()

        return HttpResponse('sended!')


class GameFavoritesView(LoginRequiredMixin, ListView):
    template_name = 'base/favourites.html'
    context_object_name = 'game_favourites'

    def get_queryset(self):
        return Game.objects.select_related('user') \
        .prefetch_related('platform').filter(favourites__slug=self.request.user.slug)
    

class GameCatalogView(ListView):
    queryset = Game.objects.select_related('user') \
        .prefetch_related('platform').order_by('-created_at')

    template_name = 'base/catalog.html'
    context_object_name = 'games'


@login_required
def add_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.add(request.user.slug)
    return HttpResponse('added')

@login_required
def remove_favourite(request, slug):
    game = get_object_or_404(Game, slug=slug)
    game.favourites.remove(request.user.slug)
    return HttpResponse('removed')

@login_required
def add_checkout(request, slug):
    item = get_object_or_404(Game, slug=slug)
    CheckoutItem.objects.get_or_create(owner=request.user)
    request.user.checkouts.add(item)
    return HttpResponse('added')

@login_required
def remove_checkout(request, slug):
    item = get_object_or_404(Game, slug=slug)
    CheckoutItem.objects.get_or_create(owner=request.user)
    request.user.checkouts.remove(item)
    return HttpResponse('removed')