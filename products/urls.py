from django.urls import path

from products.views import ListView, DetailView, CreateView

urlpatterns = [
    path('', ListView.as_view() , name='product-list'),
    path('<int:pk>/', DetailView.as_view() , name='product-detail'),
    path('create/', CreateView.as_view() , name='product-create'),
]
