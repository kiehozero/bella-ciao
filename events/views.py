from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (
    get_object_or_404, HttpResponse, redirect, render, reverse)

from .forms import EventForm
from .models import Event, EventAttendees
from profiles.models import UserProfile


@login_required
def all_events(request):
    """ Display list of events """
    events = Event.objects.all().order_by('date')
    template = 'events/events.html'
    context = {
        'events': events,
    }

    return render(request, template, context)


@login_required
def view_event(request, event_id):
    """ Display more information to the user """
    """ Display an admin panel for admins """
    event = get_object_or_404(Event, pk=event_id)
    attendees = EventAttendees.objects.filter(
        event=event).values_list().order_by('user')
    guestlist = []

    for attendee in attendees:
        # stores event_attendee pk to pass to delete_attendee if required
        username = User.objects.get(pk=attendee[1])
        guestlist.append(
            {'user': attendee[1], 'username': username, 'attendee_key': attendee[0]}
        )
    template = 'events/view_event.html'
    context = {
        'event': event,
        'guestlist': guestlist,
    }
    # access attendees db here to give a countdown of tickets remaining,
    # will need to return event.capacity, then filter attendees by event_id,
    # then substract. Also run a percentage remaining sum that turns the text
    # red when it is closer to selling out (define % threshold in settings.py)
    # write this function in a profile_tools.py file
    return render(request, template, context)


@login_required
def join_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect(reverse('home'))
    event = get_object_or_404(Event, pk=event_id)
    profile = UserProfile.objects.get(user=request.user)
    user = profile.user
    # needs to search for user/event combo already being in DB
    EventAttendees.objects.create(user=user, event=event)
    messages.info(
        request, f"You're in! {event.event_name} \
            has been added to your events.")
    return redirect(reverse('view_event', args=[event.id]))
    # need to redirect back to 'events' if that was the request source
    # in join_event, if Event Attendees already contains this number of
    # attendees defined in capacity, users will get a Sold Out message)


@login_required
def add_event(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.info(
                request, f'{event.event_name} added to events.')
            return redirect(reverse('view_event', args=[event.id]))
        else:
            messages.error(
                request, "Item addition failure. Please \
                    check your submission for errors."
            )
    else:
        form = EventForm()
    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Admin-only view to edit an existing event """
    event = get_object_or_404(Event, pk=event_id)
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.info(
                request, f'Updated {event.event_name}')
            return redirect(reverse('view_event', args=[event.id]))
        else:
            messages.error(
                request, "Event update failure. Please \
                    check your submission for errors."
            )
    else:
        form = EventForm(instance=event)

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }
    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)

    event.delete()
    messages.info(request, "Event deleted.")

    return redirect(reverse('events'))


@login_required
def delete_attendee(request, attendee_key):
    """ Admin-only feature to delete a user from an event """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    attendee = EventAttendees.objects.get(pk=attendee_key)
    attendee.delete()
    messages.info(
        request, "User removed from event")

    return redirect(reverse('events'))
