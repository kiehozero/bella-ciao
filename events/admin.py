from django.contrib import admin
from .models import Event, EventAttendees


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name', 'location',
        'category', 'date', 'capacity',
    )

    ordering = ('date',)


class EventAttendeesAdmin(admin.ModelAdmin):
    list_display = ('event', 'user',)

    ordering = ('event', 'user',)


admin.site.register(Event, EventAdmin)
admin.site.register(EventAttendees, EventAttendeesAdmin)
