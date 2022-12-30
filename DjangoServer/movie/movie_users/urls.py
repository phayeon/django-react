from django.urls import re_path as url

from movie.movie_users import views

urlpatterns = [
    url(r'movieuser$', views.movieuser),
    url(r'movieuser_list-list', views.movieuser_list)
]