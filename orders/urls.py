from django.urls import path

from orders.views import ListView, DetailView, CreateView, CreateOrderProductsView

urlpatterns = [
    path('', ListView.as_view() , name='order-list'),
    path('<int:pk>/', DetailView.as_view() , name='order-detail'),
    path('create/', CreateView.as_view() , name='order-create'),
    path('order/<int:pk>/', CreateOrderProductsView.as_view() , name='order-products'),
]
