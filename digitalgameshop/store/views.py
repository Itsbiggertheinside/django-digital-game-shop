from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count, ExpressionWrapper, F, FloatField, PositiveIntegerField, Q, Sum
from .models import Game, Order, OrderItem
from .submodels import GameImage, Comment
from .forms import CommentForm



class GameIndexView(View):
    
    def get(self, request, *args, **kwargs):
        game = Game.objects.all()

        top_rated = game.prefetch_related('genres', 'languages', 'platforms').exclude(
            status='PRE_ORDER'
        ).annotate(
            rating= ExpressionWrapper(F('metascore') * Count('favourites'), output_field= PositiveIntegerField())
        ).order_by('-rating')[:5]

        latest_released = game.prefetch_related('platforms').filter(
            status='ON_SALE'
        )[:10]

        pre_ordered = game.prefetch_related('platforms').filter(
            status='PRE_ORDER'
        )[:10]

        context = {
            'rated': top_rated,
            'latest': latest_released,
            'pre': pre_ordered,
        }
        return render(request, 'store/home.html', context)


class GameDetailView(DetailView):
    queryset = Game.objects.prefetch_related('genres', 'languages', 'platforms').all()
    template_name = 'store/detail.html'
    context_object_name = 'game'

    def get_context_data(self, **kwargs):
        context = super(GameDetailView, self).get_context_data(**kwargs)

        context['images'] = GameImage.objects.select_related('game').filter(game__id=self.get_object().id)
        context['comments'] = Comment.objects.select_related('parent', 'author').filter(parent__id=self.get_object().id)
        context['form'] = CommentForm
        context['latest'] = Game.objects.filter(status='ON_SALE').order_by('-release_date')[:10]

        return context

    @login_required
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST or None)

        if form.is_valid():
            parent = self.get_object()
            user = request.user
            comment = form.cleaned_data.get('comment')
            send = Comment(parent=parent, author=user, comment=comment)
            send.save()
            return redirect(parent.get_absolute_url())


class GameFavouritesView(LoginRequiredMixin, ListView):
    template_name = 'store/favourites.html'
    context_object_name = 'games'

    def get_queryset(self):
        return Game.objects.prefetch_related('platforms').filter(
            favourites__id=self.request.user.id)


class GameCatalogView(ListView):
    queryset = Game.objects.prefetch_related('platforms').order_by('-created_at')
    template_name = 'store/catalog.html'
    context_object_name = 'games'


class CheckoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        items = OrderItem.objects.select_related('order', 'item').filter(order__owner=self.request.user)
        total_price = items.annotate(counted_price=ExpressionWrapper(
            F('item__price') * F('quantity'), output_field= FloatField()
            )).values('counted_price').aggregate(total=Sum('counted_price'))['total']
        

        context = { 'items': items, 'total_price': total_price, }
        return render(request, 'store/checkout.html', context)


def contact(request):
    return render(request, 'store/contacts.html')

# -------------------------------------------------------------------------------


@login_required
def add_favourite(request, id=None):
    game = get_object_or_404(Game, id=id)
    game.favourites.add(request.user.id)
    return JsonResponse({'success': 'e eklendi'}, status=200)

@login_required
def remove_favourite(request, id=None):
    game = get_object_or_404(Game, id=id)
    game.favourites.remove(request.user.id)
    return JsonResponse({'success': 'den çıkartıldı'}, status=200)

@login_required
def add_to_order(request, id=None):
    game = get_object_or_404(Game, id=id)
    order, created = Order.objects.get_or_create(owner=request.user)
    order_item, created = OrderItem.objects.get_or_create(order=order, item=game)
    order_item.quantity += 1
    order_item.save()
    return JsonResponse({'success': 'ok'}, status=200)

@login_required
def plus_quantity(request, id=None):
    order_item = get_object_or_404(OrderItem, id=id)
    order_item.quantity += 1
    order_item.save()
    return JsonResponse({'quantity': order_item.quantity}, status=200)

@login_required
def less_quantity(request, id=None):
    order_item = get_object_or_404(OrderItem, id=id)
    order_item.quantity -= 1
    order_item.save()
    return JsonResponse({'quantity': order_item.quantity}, status=200)

@login_required
def remove_item(request, id=None):
    order_item = get_object_or_404(OrderItem, id=id)
    order_item.delete()
    return JsonResponse({'success': 'ok'}, status=200)
