from rest_framework.decorators import api_view
from shop.deliveries.repositories import DeliveriesRepository
from shop.deliveries.serializers import DeliveriesSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def deliveries(request):
    if request.method == "GET":
        return DeliveriesRepository().find_by_Deliveries(request.data)
    elif request.method == "POST":
        return DeliveriesSerializer().create(request.data)
    elif request.method == "PUT":
        return DeliveriesSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return DeliveriesSerializer().delete(request.data)


@api_view(['GET'])
def deliveries_list(request):
    return DeliveriesRepository().get_all(request.data)

