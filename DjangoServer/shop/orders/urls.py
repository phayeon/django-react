from django.urls import re_path as url
from shop.orders import views

urlpatterns = [
    url(f'order$', views.order),
    url(f'order-list', views.order_list)
]