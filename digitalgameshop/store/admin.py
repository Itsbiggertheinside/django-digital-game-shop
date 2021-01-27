from django.contrib import admin
from .models import Game
from .submodels import GameImage, Comment

# Register your models here.
class GameImageInline(admin.TabularInline):
    model = GameImage
    extra = 1


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name', 'price', 'status', 'release_date',)
    list_display_links = ('name',)
    list_editable = ('status',)
    ordering = ('-created_at',)
    inlines = (GameImageInline,)


admin.site.register(Game, GameAdmin)