from django.urls import re_path as url
from blog.comment import views

urlpatterns = [
    url(r'comment$', views.comment),
    url(r'comment-list', views.comment_list)
]