from django.urls import path
from .views import (GameHomeView, 
                    GameDetailView, 
                    GameFavoritesView,
                    GameCatalogView,
                    add_favourite,
                    remove_favourite,
                    add_checkout, 
                    remove_checkout)

app_name = 'game'

urlpatterns = [

    path('', GameHomeView.as_view(), name='home'),
    path('catalog/', GameCatalogView.as_view(), name='catalog'),
    path('game/detail/<slug:slug>/', GameDetailView.as_view(), name='detail'),
    
    path('favourites/', GameFavoritesView.as_view(), name='favourites'),
    path('game/favourite/add/<slug:slug>', add_favourite, name='add-favourite'),
    path('game/favourite/remove/<slug:slug>', remove_favourite, name='remove-favourite'),
    
    path('game/checkout/add/<slug:slug>/', add_checkout, name='add-checkout'),
    path('game/checkout/remove/<slug:slug>/', remove_checkout, name='remove-checkout'),
    
]
