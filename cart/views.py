from django.shortcuts import redirect, render, reverse


def view_cart(request):
    """ See the contents (if any) of the shopping cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of given item to cart. If a cart
    exists, it updates it, if not it creates it """

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
                # update item quantity if item/size combination already exists
                cart[item_id]['items_by_size'][size] += quantity
            else:
                # set quantity if item/size combination doesn't exist
                cart[item_id]['items_by_size'][size] = quantity
        else:  # sets new item if it has size but item_id isn't yet in cart
            cart[item_id] = {'items_by_size': {size: quantity}}
    else:  # for items with no size
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Add quantity of given item to cart. If a cart
    exists, it updates it, if not it creates it """

    quantity = int(request.POST.get('quantity'))

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
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
        else:
            del cart[item_id]['items_by_size'][size]
    else:  # for items with no size
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop[item_id]

    request.session['cart'] = cart

    return redirect(reverse('view_cart'))
