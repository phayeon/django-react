from django.urls import re_path as url
from shop.products import views

urlpatterns = [
    url(f'product$', views.product),
    url(f'product-list', views.product_list)
]