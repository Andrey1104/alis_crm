from django.urls import path, re_path

from sales import consumers
from sales.views import OrderListView, OrderCreateView


app_name = 'sales'

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order_list"),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
]
