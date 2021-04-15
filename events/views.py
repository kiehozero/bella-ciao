from django.shortcuts import get_object_or_404, render
# from .models import Events, EventAttendees
# # add forms.py to create new events


def view_events(request):
    """ Display list of events """
    return render(request, 'events/events.html')


# def event_detail(request, event_id):
#     """ Display more information to the user """
#     """ Display an admin panel for admins """
#     event = get_object_or_404(Events, event_id=event_id)
#     template = 'events/event_detail.html'
#     context = {
#         'event': event,
#     }
#     return render(request, template, context)


# def join_event(request, event_id):
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

# def delete_event(request, event_id):
#     template = 'events/delete_event.html'
#     context = {
#         'event': event,
#     }
#     return render(request, template, context)