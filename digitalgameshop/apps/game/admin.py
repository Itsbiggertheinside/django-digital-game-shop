from django.contrib import admin
from .models import Game, GameImage, GameRatings

# Register your models here.
class InlineGameImage(admin.StackedInline):
    model = GameImage
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'developer', 'release_date', 'on_sale', 'pre_order',)
    list_editable = ('on_sale', 'pre_order', )
    list_per_page = 15
    inlines = (InlineGameImage, )

admin.site.register(GameRatings)