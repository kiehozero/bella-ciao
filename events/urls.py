from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_events, name='events'),
    # admin view of events
    # admins view of event attendees
]
