from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('add_product/', views.add_product, name='add_product'),
    path(
        'delete_product/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path(
        'edit_product/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path('<int:product_id>/', views.view_product, name='view_product'),
]
