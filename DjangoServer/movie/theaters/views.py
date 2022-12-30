from rest_framework.decorators import api_view
from movie.theaters.repositories import TheaterRepository
from movie.theaters.serializers import TheaterSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def theater(request):
    if request.method == "GET":
        return TheaterRepository().find_by_theater(request.data)
    elif request.method == "POST":
        return TheaterSerializer().create(request.data)
    elif request.method == "PUT":
        return TheaterSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheaterSerializer().delete(request.data)


@api_view(['GET'])
def theater_list(request):
    return TheaterRepository().get_all(request.data)

