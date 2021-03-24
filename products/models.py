from django.db import models
# format is taken from the Boutique Ado project and customised accordingly


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    render_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_render_name(self):
        return self.render_name


class Product(models.Model):
    # metaclass here overrides the default Django
    # behaviour of just adding an 's' to the model name

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
