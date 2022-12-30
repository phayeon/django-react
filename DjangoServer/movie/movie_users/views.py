from rest_framework.decorators import api_view

from movie.movie_users.repositories import MovieUserRepository
from movie.movie_users.serializers import MovieUserSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def movieuser(request):
    if request.method == "GET":
        return MovieUserRepository().find_by_MovieUser(request.data)
    elif request.method == "POST":
        return MovieUserSerializer().create(request.data)
    elif request.method == "PUT":
        return MovieUserSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return MovieUserSerializer().delete(request.data)


@api_view(['GET'])
def movieuser_list(request):
    return MovieUserRepository().get_all(request.data)
