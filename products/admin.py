from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'category',
        'name',
        'price',
        'image',
    )

    ordering = ('name', 'category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'render_name',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

