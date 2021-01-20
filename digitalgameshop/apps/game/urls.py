from django.urls import path
from .views import GameHomeView, GameDetailView, GameFavoritesView

app_name = 'game'

urlpatterns = [

    path('', GameHomeView.as_view(), name='home'),
    path('game/detail/<slug:slug>/', GameDetailView.as_view(), name='detail'),
    path('favourites/', GameFavoritesView.as_view(), name='favorites'),
    
]
