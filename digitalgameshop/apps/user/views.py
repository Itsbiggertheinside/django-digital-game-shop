from django.shortcuts import render
from django.views.generic import DetailView
from .models import Account

# Create your views here.
class ProfileDetailView(DetailView):
    model = Account
    template_name = 'account/profile'
    context_object_name = 'user'