from rest_framework.response import Response
from movie.movie_users.models import Movie_user
from movie.movie_users.serializers import MovieUserSerializer


class MovieUserRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(MovieUserSerializer(Movie_user.objects.all(), many=True).data)

    def find_by_MovieUser(self):
        return Response(MovieUserSerializer(Movie_user.objects.all(), many=True).data)
