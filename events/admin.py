from django.contrib import admin
from .models import Event  #, EventAttendees


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name', 'location', 'category',
        'description', 'date', 'capacity', 'image',
    )

    ordering = ('event_name',)


admin.site.register(Event, EventAdmin)
# admin.site.register(EventAttendees, EventAttendeesAdmin)
