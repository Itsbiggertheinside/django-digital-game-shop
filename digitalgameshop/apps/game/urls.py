from django.urls import path
from .views import (GameHomeView, 
                    GameDetailView, 
                    GameFavoritesView,
                    add_favourite,
                    remove_favourite,)

app_name = 'game'

urlpatterns = [

    path('', GameHomeView.as_view(), name='home'),
    path('game/detail/<slug:slug>/', GameDetailView.as_view(), name='detail'),
    path('game/favourite/add/<slug:slug>', add_favourite, name='add-favourite'),
    path('game/favourite/remove/<slug:slug>', remove_favourite, name='remove-favourite'),
    path('favourites/', GameFavoritesView.as_view(), name='favourites'),
    
]
