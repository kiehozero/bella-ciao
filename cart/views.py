from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render, reverse

from products.models import Product

def view_cart(request):
    """ See the contents (if any) of the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of given item to cart. If a cart
    exists, it updates it, if not it creates it """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    size = None
    flavour = None
    milk = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if 'product_milk' in request.POST:
        milk = request.POST['product_milk']
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']

    cart = request.session.get('cart', {})

    # below if statement needs to be extended to include flavour and milk
    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                # sets item quantity if item/size combination already exists
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Added {product.name} to cart.')
            else:
                # set quantity if item/size combination doesn't exist
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added {product.name} to cart.')
        else:  # sets new item if it has size but item_id isn't yet in cart
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added {product.name} to cart.')
    else:  # for items with no size
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Added {product.name} to cart.')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to cart.')

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Update quantity of a given item then post the new quantity to the
    cart. Also possible to remove an item by setting quantity to zero. """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))

    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    milk = None
    if 'product_milk' in request.POST:
        milk = request.POST['product_milk']
    flavour = None
    if 'product_flavour' in request.POST:
        flavour = request.POST['product_flavour']

    cart = request.session.get('cart', {})

    # below if statement needs to be extended to include flavour and milk
    # perhaps it would be good to combine them into keys, e.g. size only,
    # size and milk, size and flavour, size milk flavour (s, sm, sf, smf)?
    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'{product.name} updated.')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'{product.name} updated.')
    else:  # for items with no size
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} updated.')
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} updated.')

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))


def remove_item(request, item_id):
    """ Remove item from the cart entirely """
    try:
        product = Product.objects.get(pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        milk = None
        if 'product_milk' in request.POST:
            milk = request.POST['product_milk']
        flavour = None
        if 'product_flavour' in request.POST:
            flavour = request.POST['product_flavour']

        cart = request.session.get('cart', {})

        # below if statement needs to be extended to include flavour and milk
        if size:
            # deletes size key if present, deletes whole item if not
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
                messages.success(request, f'{product.name} removed from your cart.')
        else:
            cart.pop(item_id)
            messages.success(request, f'{product.name} removed from your cart.')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
