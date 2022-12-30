from django.urls import re_path as url
from shop.deliveries import views

urlpatterns = [
    url(f'deliveries$', views.deliveries),
    url(f'deliveries-list', views.deliveries_list)
]