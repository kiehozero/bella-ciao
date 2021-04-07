from django.http import HttpResponse


class stripeWH_handler:
    def __init__(self, request):
        """ Handle Stripe webhooks """
        self.request = request

    def handle_event(self, event):
        """ Handle all other webhooks """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
