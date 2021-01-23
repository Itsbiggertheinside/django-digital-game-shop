from django.contrib import admin
from .models import Game, GameImage, GameRatings, Comment

# Register your models here.
class InlineGameImage(admin.StackedInline):
    model = GameImage
    extra = 1

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'developer', 'release_date', 'status',)
    list_editable = ('status',)
    list_per_page = 15
    inlines = (InlineGameImage, )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Comment)