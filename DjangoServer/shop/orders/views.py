from rest_framework.decorators import api_view
from shop.orders.repositories import OrdersRepository
from shop.orders.serializers import OrdersSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def order(request):
    if request.method == "GET":
        return OrdersRepository().find_by_Orders(request.data)
    elif request.method == "POST":
        return OrdersSerializer().create(request.data)
    elif request.method == "PUT":
        return OrdersSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return OrdersSerializer().delete(request.data)


@api_view(['GET'])
def order_list(request):
    return OrdersRepository().get_all(request.data)

