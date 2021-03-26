from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Product


def all_products(request):
    """ Display all items """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET['search']:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ Display all information on a particular products """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)
