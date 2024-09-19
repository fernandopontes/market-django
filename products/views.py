from django.shortcuts import redirect
from django.views import generic
from products.forms import ProductForm
from products.models import Product

class ListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

class DetailView(generic.DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/detail.html'

class CreateView(generic.FormView):
    template_name = 'products/create.html'
    form_class = ProductForm
    success_url = '/products/create/'

    def form_valid(self, form):
        if(form.is_valid()):
            form.save()
            return redirect('product-list')
        return super().form_valid(form)