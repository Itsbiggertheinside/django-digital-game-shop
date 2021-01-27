from django.urls import path
from .views import (
    GameIndexView,
    GameDetailView, 
    GameFavouritesView,
    GameCatalogView,
    add_favourite,
    remove_favourite,
    )

urlpatterns = [
    
    path('', GameIndexView.as_view(), name='home'),
    path('catalog/', GameCatalogView.as_view(), name='catalog'),
    path('game/detail/<slug:slug>/', GameDetailView.as_view(), name='detail'),
    
    path('favourites/', GameFavouritesView.as_view(), name='favourites'),
    path('game/favourite/add/<int:id>', add_favourite, name='add-favourite'),
    path('game/favourite/remove/<int:id>', remove_favourite, name='remove-favourite'),

]
