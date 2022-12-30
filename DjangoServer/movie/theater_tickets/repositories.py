from rest_framework.response import Response

from movie.theater_tickets.models import TheaterTicket
from movie.theater_tickets.serializers import TheaterTicketSerializer


class TheaterTicketRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(TheaterTicketSerializer(TheaterTicket.objects.all(), many=True).data)

    def find_by_theaterTicket(self):
        return Response(TheaterTicketSerializer(TheaterTicket.objects.all(), many=True).data)
