from django.urls import re_path as url

from dlearn import views

urlpatterns = [
    url(r'irispost', views.iris_Post),
    url(r'irisget', views.iris_Get),
    url(r'stroke', views.stroke),
    url(r'fashion', views.fashion),
    url(r'aitrader-post', views.aiTrader_Post)
]
