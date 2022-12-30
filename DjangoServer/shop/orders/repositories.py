from rest_framework.response import Response

from shop.orders.models import Orders
from shop.orders.serializers import OrdersSerializer


class OrdersRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(OrdersSerializer(Orders.objects.all(), many=True).data)

    def find_by_Orders(self):
        return Response(OrdersSerializer(Orders.objects.all(), many=True).data)
