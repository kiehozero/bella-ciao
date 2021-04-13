from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import ProductForm
from .models import Product, Category


def all_products(request):
    """ Display all items """
    products = Product.objects.all()

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
    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sort': current_sort,
        'cat_list': cat_list,
    }

    return render(request, template, context)


def view_product(request, product_id):
    """ Display all information on a particular products """
    product = get_object_or_404(Product, pk=product_id)
    template = 'products/view_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


def add_product(request):
    """ Admin-only view to add item to the store """
    """ need to replicate this for categories and events """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f'{product.name} added to store.')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(
                request, "Item addition failure. Please \
                    check your submission for errors."
            )
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Admin-only view to edit an item in the store """
    """ need to replicate this for categories and events """
    product = get_object_or_404(Product, pk=product_id)
    # add link to this view in product_detail page
    # change admin page to a central link for CRUD ops by admin
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Updated {product.name}')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(
                request, "Item update failure. Please \
                    check your submission for errors."
            )
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Admin-only view to delete an item from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted.")
    return redirect(reverse('products'))
