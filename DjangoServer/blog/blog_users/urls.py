from django.urls import re_path as url
from blog.blog_users import views

urlpatterns = [
    url(r'login', views.login),
    url(r'user-list', views.blog_user_list),
    url(r'user-create', views.user_create),
    url(r'blog-user', views.blog_user)
]