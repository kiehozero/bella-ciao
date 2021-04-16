from django import forms
from django.contrib.admin import widgets 

from .models import Event


class EventForm(forms.ModelForm):
    """ allows admins to create an event in add_event """
    class Meta:
        model = Event
        fields = '__all__'
    # need to make the description field bigger
    # need date field widget to be input type date or have a placeholder
