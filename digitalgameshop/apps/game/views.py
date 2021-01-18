from django.shortcuts import render
from django.views.generic import ListView
from .models import Game

# Create your views here.
class HomeView(ListView):
    queryset = Game.objects.select_related('user').prefetch_related('genres', 'languages', 'platform').all()
    template_name = 'base/home.html'

        
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['queryset'] = self.queryset
        return context
    