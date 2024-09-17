from django import forms

from products.models import Product

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'