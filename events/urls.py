from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_events, name='events'),
    path('<int:event_id>/', views.view_event, name='view_event'),
    path(
        'delete_event/<int:event_id>/',
        views.delete_event,
        name='delete_event'),
    # path('edit_event/', views.edit_event, name='edit_event'),
    # path('join_event/', views.join_event, name='join_event'),
]
