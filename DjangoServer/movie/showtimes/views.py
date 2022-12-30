from rest_framework.decorators import api_view

from movie.showtimes.repositories import ShowtimeRepository
from movie.showtimes.serializers import ShowtimeSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def showtime(request):
    if request.method == "GET":
        return ShowtimeRepository().find_by_showtime(request.data)
    elif request.method == "POST":
        return ShowtimeSerializer().create(request.data)
    elif request.method == "PUT":
        return ShowtimeSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ShowtimeSerializer().delete(request.data)


@api_view(['GET'])
def showtime_list(request):
    return ShowtimeRepository().get_all(request.data)
