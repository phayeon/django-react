from django.urls import re_path as url
from movie.movies import views

urlpatterns = [
    url(f'fake-faces', views.faces),
    url(f'movies$', views.movies),
    url(f'movie-list', views.movie_list)
]