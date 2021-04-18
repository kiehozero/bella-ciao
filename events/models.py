from django.db import models


class Event(models.Model):
    """ Index of upcoming in-store events """
    event_name = models.CharField(max_length=30, null=False, blank=False)
    location = models.CharField(max_length=30, null=False, blank=False)
    category = models.CharField(max_length=15, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    date = models.DateTimeField(null=True, blank=True)
    capacity = models.IntegerField(null=False, blank=False, default=0)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.event_name


class EventAttendees(models.Model):
    """ Index of attendees at upcoming in-store events """
    user = models.CharField(max_length=30, null=False, blank=False)
    event = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'User {self.user} at event {self.event}'
