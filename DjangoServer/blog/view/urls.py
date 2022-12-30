from django.urls import re_path as url
from blog.view import views

urlpatterns = [
    url(r'views$', views.views),
    url(r'views-list', views.views_list)
]