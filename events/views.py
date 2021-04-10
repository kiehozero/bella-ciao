from django.shortcuts import render


def view_events(request):
    """ Display list of events """
    return render(request, 'events/events.html')
