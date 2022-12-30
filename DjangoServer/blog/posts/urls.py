from django.urls import re_path as url
from blog.posts import views

urlpatterns = [
    url(r'post$', views.post),
    url(r'post-list', views.post_list)
]