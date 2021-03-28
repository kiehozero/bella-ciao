from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    # replicate below logic to tell customer how many coffees they have
    # until a free one and then also to create a free coffee button for
    # eligible users that subtracts eligible items from the subtotal

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
