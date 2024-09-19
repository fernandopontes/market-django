from django.urls import path

from api.views import OrderCreateAPIView

urlpatterns = [
    path('orders/', OrderCreateAPIView.as_view(), name='api-order-create'),
]
