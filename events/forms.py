from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    """ allows admins to create an event in add_event """
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-green'