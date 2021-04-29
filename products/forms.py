from django import forms

from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Admin form to add new products to store """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        render_names = [(
            item.id, item.get_render_name()) for item in categories]

        self.fields['category'].choices = render_names
        self.fields['price'].widget.attrs['min'] = '0.10'
        self.fields['price'].widget.attrs['step'] = '0.10'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-green'
