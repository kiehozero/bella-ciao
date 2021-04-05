from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm


def checkout(request):
    """ See the contents (if any) of the shopping cart """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ISPN5AbTLswkfEnRMl1vGz6pty9s4oBG0BmmrbfguKdw61pk8STD9g9VZEZHyZrGDGW8wSYu9kcxw1WeLIc4Zze00EPXtrtpH',
        'client_secret': 'test_client_secret',
    }
    return render(request, template, context)
