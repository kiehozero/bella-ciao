from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from cart.contexts import cart_contents
from .forms import OrderForm

import stripe


# core logic comes from Boutique Ado tutorial
def checkout(request):
    """ See the contents (if any) of the shopping cart """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
