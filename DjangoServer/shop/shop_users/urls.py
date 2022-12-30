from django.urls import re_path as url
from shop.shop_users import views

urlpatterns = [
    url(f'shopuser$', views.shopUser),
    url(f'shopuser-list', views.shopUser_list)
]