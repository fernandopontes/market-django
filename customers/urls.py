from django.urls import path

from customers.views import ListView, DetailView, CreateView

urlpatterns = [
    path('', ListView.as_view() , name='customer-list'),
    path('<int:pk>/', DetailView.as_view() , name='customer-detail'),
    path('create/', CreateView.as_view() , name='customer-create'),
]
