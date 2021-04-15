from django.db import models

# class Event(models.Model):

### event_name = models.CharField(max_length=30, null=False, blank=False)
### location = models.CharField(max_length=30, null=False, blank=False)
### category = models.CharField(max_length=15, null=False, blank=False)
### description = models.CharField(max_length=500, null=False, blank=False)
### date = models.DateFimeField(null=True, blank=True)
### capacity = models.IntegerField(null=False, blank=False, default=0)
### image = models.ImageField(null=True, blank=True)

### use calendar picker for filling out date
### display generic CBC logo if no image is present
### in join_event, if the Event Attendees already contains this number
### of attendees defined in capacity, users will get a Sold Out message)

# class EventAttendees(models.Model):

### username = models.CharField(max_length=30, null=False, blank=False)
### event = models.CharField(max_length=30, null=False, blank=False)

### join_event view adds both the user's username and the event item requested

### to view their own events, user profile will need to import EventAttendees and
### return any entries where a matching username is found