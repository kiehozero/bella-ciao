from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import EventForm
from .models import Event
# , EventAttendees
# # add forms.py to create new events


def all_events(request):
    """ Display list of events """
    events = Event.objects.all().order_by('date')
    # need to sort by event.date
    template = 'events/events.html'
    context = {
        'events': events,
    }

    return render(request, template, context)


def view_event(request, event_id):
    """ Display more information to the user """
    """ Display an admin panel for admins """
    event = get_object_or_404(Event, pk=event_id)
    template = 'events/view_event.html'
    context = {
        'event': event,
    }
    return render(request, template, context)


# def join_event(request, event_id):
#     if not request.user.is_authenticated:
#         return redirect(reverse('home'))
#     # will be similar to add to cart process
#     template = 'events/join_event.html'
#     context = {
#         'event': event,
#     }
#     return render(request, template, context)
#     in join_event, if the Event Attendees already contains this number
#     of attendees defined in capacity, users will get a Sold Out message)


@login_required
def add_event(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.info(
                request, f'{event.event_name} added to store.')
            return redirect(reverse('view_product', args=[event.id]))
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


# def event_attendees(request):
