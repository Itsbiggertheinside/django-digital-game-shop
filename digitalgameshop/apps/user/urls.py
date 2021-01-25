from django.urls import path
from .views import ProfileDetailView, CheckoutListView

urlpatterns = [

    path('profile/<slug:slug>/', ProfileDetailView.as_view(), name='profile'),
    path('checkout/<slug:slug>/', CheckoutListView.as_view(), name='checkout'),


]
