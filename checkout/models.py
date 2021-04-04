from django.conf import settings
from django.db import models
from django.db.models import Sum

from products.models import Product

import uuid


class Order(models.Model):
    order_number = models.CharField(max_length=12, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    phone_number = models.CharField(max_length=12, null=False, blank=False)
    eircode = models.CharField(max_length=7, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=False)
    # need to add site here? Four sites plus delivery
    loyalty_stamps = models.IntegerField(null=False, blank=False, default=0)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=10, null=True, blank=True)  # not all products contain this
    product_milk = models.CharField(max_length=20, null=True, blank=True)
    product_flavour = models.CharField(max_length=30, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)
