from django.urls import path, re_path

from sales import consumers
from sales.views import OrderListView, OrderCreateView, projection_view

app_name = 'sales'

urlpatterns = [
    path("orders/", OrderListView.as_view(), name="order_list"),
    path('orders/create/', OrderCreateView.as_view(), name='order_create'),
    path("projection/", projection_view, name="projection"),
]
