from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order, OrderLineItem
from events.models import Event, EventAttendees

import datetime


@login_required
def profile(request):
    """ Show the user's profile """

    # basic information
    time = datetime.datetime.now()
    profile = get_object_or_404(UserProfile, user=request.user)
    # returns user's first name if they have saved it
    if profile.default_name is not None:
        default_name = profile.default_name
        forename = default_name.title().split(" ")[0]
    else:
        forename = "friend"

    # Update profile information
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

    # Order and Event histories
    orders = profile.orders.all()
    events_attending = EventAttendees.objects.filter(
        user=request.user).values_list()
    events_list = []
    for event in events_attending:
        events_list.append(event[2])
    events = Event.objects.filter(pk__in=events_list)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'events': events,
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


@login_required
def admin(request):
    template = 'profiles/admin.html'
    return render(request, template)
