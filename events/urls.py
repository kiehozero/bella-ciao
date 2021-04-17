from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.view_event, name='view_event'),
    path('add_event/', views.add_event, name='add_event'),
    path(
        'delete_event/<int:event_id>/',
        views.delete_event,
        name='delete_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
    # path(
    #     'event_attendees/<int:event_id>/',
    #     views.event_attendees,
    #     name='event_attendees'),
    path('join_event/<int:event_id>/', views.join_event, name='join_event'),
]
