from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse
from .models import Product, Category


def all_products(request):
    """ Display all items """
    products = Product.objects.all()
    all_cats = Category.objects.all()
    all_cat_names = all_cats.annotate(lower_name=Lower('name'))
    # Bugfix #1: use cat_list to extract category name before it enters
    # QuerySet, then use this to highlight category name upon use as filter
    categories = None
    cat_list = None
    query = None
    sort = None
    direction = None

    # sorting logic taken from Boutique Ado project
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            cat_list = categories[0]
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sort = f'{sort}_{direction}'

    # will need to go back to MS3 to find out how to
    # reset the search criteria to show all products

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sort,
        'cat_list': cat_list,
        'all_cat_names': all_cat_names,
    }

    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """ Display all information on a particular products """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)
