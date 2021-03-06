from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, reverse

from .forms import UserProfileForm
from .models import UserProfile
from checkout.models import Order, OrderLineItem
from events.models import Event, EventAttendees

import datetime
import json


@login_required
def profile(request):
    """ Show the user's profile """
    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    # User Information
    time = datetime.datetime.now()
    in_profile = True  # customises post-purchase button
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
    orders = profile.orders.all().order_by('-date')
    events_attending = EventAttendees.objects.filter(
        user=request.user).values_list()
    events_list = []
    events_dict = []
    for event in events_attending:
        events_list.append(event[2])
        event_return = Event.objects.filter(
            pk=event[2]).values(
                'event_name', 'date', 'location')
        events_dict.append({
            'event': event[2],
            'event_name': event_return[0]['event_name'],
            'attendee_key': event[0],
            'date': event_return[0]['date'],
            'location': event_return[0]['location']
            })

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'events_dict': events_dict,
        'time': time,
        'forename': forename,
        'in_profile': in_profile,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    from_profile = True

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': from_profile,
    }

    return render(request, template, context)


@login_required
def admin(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    template = 'profiles/admin.html'
    return render(request, template)


@login_required
def delete_attendance(request, attendee_key):
    """ user feature to delete event from their profile """
    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    attendee = EventAttendees.objects.get(pk=attendee_key)
    attendee.delete()
    messages.info(
        request, "Event removed from your schedule")
    return redirect('profile')
