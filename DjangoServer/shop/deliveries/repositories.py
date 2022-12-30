from rest_framework.response import Response

from shop.deliveries.models import Deliveries
from shop.deliveries.serializers import DeliveriesSerializer


class DeliveriesRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(DeliveriesSerializer(Deliveries.objects.all(), many=True).data)

    def find_by_Deliveries(self):
        return Response(DeliveriesSerializer(Deliveries.objects.all(), many=True).data)
