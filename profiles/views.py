from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order, OrderLineItem

import datetime


@login_required
def profile(request):
    """ Show the user's profile """

    time = datetime.datetime.now()
    profile = get_object_or_404(UserProfile, user=request.user)
    # returns user's first name if they have saved it
    if profile.default_name is not None:
        default_name = profile.default_name
        forename = default_name.title().split(" ")[0]
    else:
        forename = "friend"

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid:
            form.save()
            messages.success(request, "Your information has been updated.")
        else:
            messages.error(
                request, 'Update failed, please check your form for errors.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'time': time,
        'forename': forename,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
