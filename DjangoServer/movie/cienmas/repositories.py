from rest_framework.response import Response
from movie.cienmas.models import Cinema
from movie.cienmas.serializers import CinemaSerializer


class CinemaRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)

    def find_by_cinema(self):
        return Response(CinemaSerializer(Cinema.objects.all(), many=True).data)
