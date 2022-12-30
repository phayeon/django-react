from rest_framework.decorators import api_view
from movie.cienmas.repositories import CinemaRepository
from movie.cienmas.serializers import CinemaSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def cinema(request):
    if request.method == "GET":
        return CinemaRepository().find_by_cinema(request.data)
    elif request.method == "POST":
        return CinemaSerializer().create(request.data)
    elif request.method == "PUT":
        return CinemaSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CinemaSerializer().delete(request.data)


@api_view(['GET'])
def cinema_list(request):
    return CinemaRepository().get_all(request.data)
