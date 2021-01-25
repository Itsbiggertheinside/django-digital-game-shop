from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView
from .models import Account, CheckoutItem


# Create your views here.
class ProfileDetailView(DetailView):
    model = Account
    template_name = 'account/profile.html'
    context_object_name = 'user'


class CheckoutListView(ListView):
    model = CheckoutItem
    template_name = 'account/checkout.html'
    context_object_name = 'items'
