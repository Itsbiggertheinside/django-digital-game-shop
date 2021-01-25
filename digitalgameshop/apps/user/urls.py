from django.urls import path
from .views import ProfileDetailView

urlpatterns = [

    path('profile/<int:id>/', ProfileDetailView.as_view(), name='profile'),

]
