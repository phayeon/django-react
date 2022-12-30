from django.urls import re_path as url
from movie.showtimes import views

urlpatterns = [
    url(f'showtime$', views.showtime),
    url(f'showtime-list', views.showtime_list)
]