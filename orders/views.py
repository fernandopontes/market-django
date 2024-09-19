from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import generic
from customers.models import Customer
from orders.forms import OrderForm
from orders.models import Order
from orders_products.models import OrderProduct
from products.forms import ProductForm
from products.models import Product

class ListView(generic.ListView):
    model = Order
    template_name = 'orders/list.html'
    context_object_name = 'orders'

class DetailView(generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/detail.html'

class CreateView(generic.FormView):
    template_name = 'orders/create.html'
    form_class = OrderForm
    success_url = '/orders/create/'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        customers = Customer.objects.all()
        self.extra_context = {'customers': customers}
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        if(form.is_valid()):
            order = form.save()
            return redirect('order-products', pk=order.id)
        return super().form_valid(form)
    
class CreateOrderProductsView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'orders/create-order-products.html'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        order_id = self.kwargs.get('pk')
        order = Order.objects.get(id=order_id)
        self.extra_context = {'order': order}
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        items_order = []
        for key in request.POST.keys():
            if key.startswith('quantity-'):
                product_id = key.split('-')[1]
                quantity = request.POST.get(key)
                if int(quantity) > 0:
                    items_order.append({'product_id': product_id, 'quantity': quantity, 'order_id': request.POST.get('order')})

        for item in items_order:
            order_product = OrderProduct(order_id=item['order_id'], product_id=item['product_id'], quantity=item['quantity'])
            order_product.save()

        return redirect('order-list')

