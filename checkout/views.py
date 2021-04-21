from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    HttpResponse, redirect, render, reverse, get_object_or_404)
from django.views.decorators.http import require_POST

from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.contexts import cart_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

import stripe
import json


# core logic comes from Boutique Ado tutorial

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            # 'loyalty_stamps': request.POST.get('loyalty_stamps'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, "Your payment could not be processed, \
                please try again later.")
        return HttpResponse(content=e, status=400)


def checkout(request):
    """ See the contents (if any) of the shopping cart """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
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
            # POINTS, HIDE POINTS IN A HIDDEN INPUT?
            request.session['save_info'] = 'save_info' in request.POST
            # request.session['loyalty_stamps'] = 'loyalty_stamps in request.POST
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
        # loyalty_stamps here also?
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_name,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'city': profile.default_city,
                    'eircode': profile.default_eircode,
                })
                # loyalty_stamps to loyalty model here
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        # loyalty_stamps
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """ Display page once order is successfully submitted """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        # add loyalty_stamps here in logic similar to if save_info below
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

    if save_info:
        profile_data = {
            'default_name': order.full_name,
            'default_phone_number': order.phone_number,
            'default_street_address1': order.street_address1,
            'default_street_address2': order.street_address2,
            'default_city': order.city,
            'default_eircode': order.eircode,
        }
        user_profile_form = UserProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(
        request, 'Order complete!')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@login_required
def admin_orders(request):
    """ View for admin to see all orders """
    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    all_orders = Order.objects.all().order_by('-date')
    template = 'checkout/admin_orders.html'
    context = {
        'all_orders': all_orders,
    }

    return render(request, template, context)
