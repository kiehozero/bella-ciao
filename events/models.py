from django.db import models
from profiles.models import UserProfile

class Event(models.Model):

    event_name = models.CharField(max_length=30, null=False, blank=False)
    location = models.CharField(max_length=30, null=False, blank=False)
    category = models.CharField(max_length=15, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    date = models.DateTimeField(null=True, blank=True)
    capacity = models.IntegerField(null=False, blank=False, default=0)
    image = models.ImageField(null=True, blank=True)


class EventAttendees(models.Model):

    user = models.CharField(max_length=30, null=False, blank=False)
    event = models.IntegerField(null=False, blank=False)

#   join_event view adds both the user's username and the event item requested
