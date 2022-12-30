from django.urls import re_path as url

from movie.cienmas import views

urlpatterns = [
    url(r'cinema$', views.cinema),
    url(r'cinema-list', views.cinema_list)
]