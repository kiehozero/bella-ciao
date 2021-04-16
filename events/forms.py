from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    """ allows admins to create an event in add_event """
    class Meta:
        model = Event
        fields = '__all__'
    # need to make the description field bigger
