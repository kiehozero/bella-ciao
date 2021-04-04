from django.shortcuts import render


def checkout(request):
    """ See the contents (if any) of the shopping cart """
    return render(request, 'checkout/checkout.html')
