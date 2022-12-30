from django.urls import re_path as url
from shop.carts import views

urlpatterns = [
    url(f'cart$', views.cart),
    url(f'cart-list', views.cart_list)
]