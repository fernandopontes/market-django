from django.shortcuts import redirect
from django.views import generic
from customers.forms import CustomerForm
from customers.models import Customer

class ListView(generic.ListView):
    model = Customer
    template_name = 'customers/list.html'
    context_object_name = 'customers'

class DetailView(generic.DetailView):
    model = Customer
    context_object_name = 'customer'
    template_name = 'customers/detail.html'

class CreateView(generic.FormView):
    template_name = 'customers/create.html'
    form_class = CustomerForm
    success_url = '/customers/create/'

    def form_valid(self, form):
        if(form.is_valid()):
            form.save()
            return redirect('customer-list')
        return super().form_valid(form)


