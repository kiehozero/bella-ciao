from django import forms
from django.contrib.admin import widgets 

from .models import Event, EventAttendees


class EventForm(forms.ModelForm):
    """ allows admins to create an event in add_event """
    class Meta:
        model = Event
        fields = '__all__'
    # need to make the description field bigger
    # need date field widget to be input type date or have a placeholder


class JoinEventForm(forms.ModelForm):
    """ creates unique username and event number entry in EventAttendees """
    class Meta:
        model = EventAttendees
        fields = '__all__'
    # will need to be posted as two hidden input fields that the user cannot see or access
