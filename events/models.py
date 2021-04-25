from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    """ Index of upcoming in-store events """
    event_name = models.CharField(max_length=30, null=False, blank=False)
    location = models.CharField(max_length=30, null=False, blank=False)
    category = models.CharField(max_length=15, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)
    capacity = models.IntegerField(null=False, blank=False, default=75)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.event_name


class EventAttendees(models.Model):
    """ Index of attendees at upcoming in-store events """
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'User {self.user.username} is \
            attending event {self.event.event_name}'
