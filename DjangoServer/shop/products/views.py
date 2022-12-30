from rest_framework.decorators import api_view
from shop.products.repositories import ProductRepository
from shop.products.serializers import ProductSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product(request):
    if request.method == "GET":
        return ProductRepository().find_by_Product(request.data)
    elif request.method == "POST":
        return ProductSerializer().create(request.data)
    elif request.method == "PUT":
        return ProductSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ProductSerializer().delete(request.data)


@api_view(['GET'])
def product_list(request):
    return ProductRepository().get_all(request.data)

