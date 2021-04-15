from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render, reverse

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
#     # will be similar to add to cart process
#     template = 'events/join_event.html'
#     context = {
#         'event': event,
#     }
#     return render(request, template, context)


# def edit_event(request, event_id):
#     template = 'events/edit_event.html'
#     context = {
#         'event': event,
#     }
#     return render(request, template, context)


def delete_event(request, event_id):
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)

    event.delete()
    messages.info(request, "Event deleted.")

    return redirect(reverse('events'))
