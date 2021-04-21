from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from products.models import Product


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    loyalty_stamps = 0
    cart = request.session.get('cart', {})

    # this loop adds up the quantity and value of items in the cart
    for item_id, item_data in cart.items():
        # if the item is not customisable, item_data
        # will simply be an integer for quantity ordered
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            if product.loyalty is True:
                loyalty_stamps += 1
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                if product.loyalty is True:
                    loyalty_stamps += quantity
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

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
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'cart': cart,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'loyalty_stamps': loyalty_stamps,
    }

    return context
