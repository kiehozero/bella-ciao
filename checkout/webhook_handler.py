from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stripe webhooks """
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle an unexpected webhook """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """ Handle successful payments """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_failed(self, event):
        """ Handle failed payments """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
