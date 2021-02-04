from django import template
from store.models import Order, OrderItem
from django.db.models import ExpressionWrapper, F, FloatField, Sum

register = template.Library()

@register.simple_tag
def calculate_total_price(request):
    items = OrderItem.objects.select_related('order', 'item').filter(order__owner=request.user)
    total_price = items.annotate(counted_price=ExpressionWrapper(
        F('item__price') * F('quantity'), output_field= FloatField()
        )).values('counted_price').aggregate(total=Sum('counted_price'))['total']
    return total_price