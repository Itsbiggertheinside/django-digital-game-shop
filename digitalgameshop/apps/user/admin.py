from django.contrib import admin
from .models import Account, CheckoutItem

# Register your models here.
admin.site.register(Account)
admin.site.register(CheckoutItem)