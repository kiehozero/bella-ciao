from django import forms
from django.contrib.admin import widgets
from django.core.validators import RegexValidator

from .models import Event, EventAttendees


class EventForm(forms.ModelForm):
    """ allows admins to create an event in add_event """
    class Meta:
        model = Event
        fields = '__all__'
    # need to make the description field bigger
    # need date field widget to be input type date or have a placeholder,
    # see products form for customisation options

    def __init__(self, *args, **kwargs):
        """ Adds some user-friendly placeholders and form styling,
        this is taken from the Boutique Ado project """
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['placeholder'] = 'yyyy-mm-dd hh:mm:ss'
        self.fields['event_name'].widget.attrs['autofocus'] = True
        self.fields['capacity'].widget.attrs['pattern'] = '^[1-9][0-9]*$'
        self.fields['capacity'].validators = [RegexValidator(
            '^[1-9][0-9]*$', 'Capacity must be greater than zero')]


class JoinEventForm(forms.ModelForm):
    """ creates unique username and event number entry in EventAttendees """
    class Meta:
        model = EventAttendees
        fields = '__all__'
