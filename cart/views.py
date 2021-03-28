from django.shortcuts import render


def view_cart(request):
    """ See the contents (if any) of the shopping cart """
    return render(request, 'cart/cart.html')
