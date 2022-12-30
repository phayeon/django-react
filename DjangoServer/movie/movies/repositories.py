from rest_framework.response import Response

from movie.movies.models import Movies
from movie.movies.serializers import MoviesSerializer


class MoviesRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(MoviesSerializer(Movies.objects.all(), many=True).data)

    def find_by_movies(self):
        return Response(MoviesSerializer(Movies.objects.all(), many=True).data)
