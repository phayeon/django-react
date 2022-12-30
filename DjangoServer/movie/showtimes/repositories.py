from rest_framework.response import Response

from movie.showtimes.models import Showtime
from movie.showtimes.serializers import ShowtimeSerializer


class ShowtimeRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(ShowtimeSerializer(Showtime.objects.all(), many=True).data)

    def find_by_showtime(self):
        return Response(ShowtimeSerializer(Showtime.objects.all(), many=True).data)
