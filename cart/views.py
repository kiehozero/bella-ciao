from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import (
    get_object_or_404, HttpResponse, redirect, render, reverse)

from products.models import Product

""" Core model design taken from Boutique Ado tutorial """


def view_cart(request):
    """ See the contents (if any) of the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of given item to cart. If a cart
    exists, it updates it, if not it creates it """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                # sets item quantity if item/size combination already exists
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request, f'{size.title()} {product.name} quantity updated')
            else:
                # set quantity if item/size combination doesn't exist
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added {size.title()} {product.name} to cart')
        else:  # sets new item if it has size but item_id isn't yet in cart
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added {size.title()} {product.name} to cart')
    else:  # for items with no size
        if item_id in list(cart.keys()):
            # no-size item already in cart
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity')
        else:
            # no-size item new to cart
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update quantity of a given item then post the new quantity to the
    cart. Also possible to remove an item by setting quantity to zero. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    cart = request.session.get('cart', {})

    if size:
        if quantity > 0:
            # quantity decreases but item still in cart
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'{size.title()} {product.name} quantity updated')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                # quantity goes from 1 to zero
                cart.pop(item_id)
                messages.success(
                    request, f'{size.title()} {product.name} removed from your cart')
    else:  # for items with no size
        if quantity > 0:
            # quantity decreases but item still in cart
            cart[item_id] = quantity
            messages.success(request, f'{product.name} quantity updated')
        else:
            # quantity goes from 1 to zero
            cart.pop(item_id)
            messages.success(request, f'{product.name} removed from your cart')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_item(request, item_id):
    """ Remove item from the cart entirely """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        cart = request.session.get('cart', {})

        if size:
            # deletes size key if present, deletes whole item if not
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(
                    request, f'{size.title()} {product.name} removed from your cart')
        else:
            cart.pop(item_id)
            messages.success(
                request, f'{product.name} removed from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
