from django.urls import re_path as url

from nlp import views

urlpatterns = [
    url(r'samsung-report', views.report_Get),
    url(r'movie-review-post', views.movie_review_post),
    url(r'korean-classify-post', views.movie_review_post)
]