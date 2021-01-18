from django.contrib import admin
from .models import Account, CheckOut, Favourite

# Register your models here.
admin.site.register(Account)
admin.site.register(Favourite)
admin.site.register(CheckOut)
