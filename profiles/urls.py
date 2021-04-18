from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('admin/', views.admin, name='admin'),
    path(
        'delete_attendance/<int:attendee_key>/',
        views.delete_attendance,
        name='delete_attendance'),
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'),
]
