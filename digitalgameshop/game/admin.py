from django.contrib import admin
from .models import Game

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'developer', 'release_date', 'on_sale', 'pre_order',)
    list_editable = ('on_sale', 'pre_order', )
    list_per_page = 15

    