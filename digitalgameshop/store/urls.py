from django.urls import path
from .views import (
    GameIndexView,
    GameDetailView, 
    GameFavouritesView,
    GameCatalogView,
    CheckoutView,
    add_favourite,
    remove_favourite,
    add_to_order,
    plus_quantity,
    less_quantity,
    remove_item,
    contact,
    )

urlpatterns = [
    
    path('', GameIndexView.as_view(), name='home'),
    path('catalog/', GameCatalogView.as_view(), name='catalog'),
    path('game/detail/<slug:slug>/', GameDetailView.as_view(), name='detail'),
    path('contact/', contact, name='contact'),
    
    path('favourites/', GameFavouritesView.as_view(), name='favourites'),
    path('game/favourite/add/<int:id>', add_favourite, name='add-favourite'),
    path('game/favourite/remove/<int:id>', remove_favourite, name='remove-favourite'),
    
    path('checkout/order', CheckoutView.as_view(), name='checkout'),
    path('checkout/order/add/<int:id>', add_to_order, name='add-to-order'),
    path('checkout/order/item/plus-quantity/<int:id>', plus_quantity, name='plus-quantity'),
    path('checkout/order/item/less-quantity/<int:id>', less_quantity, name='less-quantity'),
    path('checkout/order/item/remove/<int:id>', remove_item, name='remove-item'),

]
