from django.urls import re_path as url
from movie.theater_tickets import views

urlpatterns = [
    url(r'theaterTicket$', views.theaterTicket),
    url(r'theaterTicket-list', views.theaterTicket_list),
    url(r'number', views.number)
]

