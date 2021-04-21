from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """ Handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send customer an email once the payment has succeeded """
        customer_email = order.email
        subject = render_to_string(
            'checkout/emails/conf-subject.txt', {'order': order}
        )

        body = render_to_string(
            'checkout/emails/conf-body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL}
        )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])

    def handle_event(self, event):
        """ Handle an unexpected webhook """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle successful payments, intent returns all customer information
        back from Stripe. If an order is submitted and the page closes before
        the success page, an order will be created using the information
        returned by the payment intent from Stripe. """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart

        save_info = intent.metadata.save_info
        # loyalty_stamps = intent.metadata.loyalty_stamps

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean up data returning by shipping_details in payment intent
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Handle save_info choices
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            # add loyalty stamps here using similar logic
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_city = shipping_details.address.city
                profile.default_eircode = shipping_details.address.postal_code
                profile.save()

        order_exists = False
        attempt = 1
        # if order is not found after 5 loops of one second each, it is created
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    eircode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f'Webhook received: {event["type"]}, \
                    verified order is already in database.'),
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    eircode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]}. ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
                content=f'Webhook received: {event["type"]}, \
                    Success: order created from webhook.',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle failed payments """
        return HttpResponse(
            content=f'Failed. Webhook received: {event["type"]}',
            status=200
        )
