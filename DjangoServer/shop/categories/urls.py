from django.urls import re_path as url
from shop.categories import views

urlpatterns = [
    url(f'categories$', views.categories),
    url(f'categories-list', views.categories_list)
]