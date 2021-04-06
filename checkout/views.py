from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render, reverse, get_object_or_404

from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from products.models import Product

import stripe


# core logic comes from Boutique Ado tutorial
def checkout(request):
    """ See the contents (if any) of the shopping cart """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # add if collection loop in here which creates a separate
        # dictionary replacing the delivery address with store name,
        # will need to refer to OrderFormCollect
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'city': request.POST['city'],
            'eircode': request.POST['eircode'],

        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                # this code is similar to cart_contents in cart/contexts.py
                try:  # if item_data is just an integer, i.e. it is sizeless
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:  # if item has sizes
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "An item in your cart could not be found."
                    ))
                    order.delete()
                    return redirect(reverse('view_cart'))

            # ALERT USE THE BELOW METHOD TO STORE LOYALTY
            # POINTS, HIDE POINT IN A HIDDEN INPUT?
            request.session['save-info'] = 'save-info' in request.POST
            return redirect(reverse(
                'checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, "There was an error submitting \
                    the order, please check your details.")
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """ Display page once order is successfully submitted """

    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(
        request, f'Order complete!')
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
