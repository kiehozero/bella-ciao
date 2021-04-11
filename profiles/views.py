from django.contrib import messages
from django.shortcuts import get_object_or_404, render

from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order, OrderLineItem

import datetime


def profile(request):
    """ Show the user's profile """

    time = datetime.datetime.now()
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, "Your information has been updated.")

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'time': time,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
