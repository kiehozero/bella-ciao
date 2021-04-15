from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_events, name='events'),
    # path('<int:event_id>/', views.event_detail, name='event_detail'),
    # path('add_event/', views.add_event, name='add_event'),
    # path('delete_event/', views.delete_event, name='delete_event'),
    # path('edit_event/', views.edit_event, name='edit_event'),
    # path('join_event/', views.join_event, name='join_event'),
]
