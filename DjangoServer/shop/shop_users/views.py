from rest_framework.decorators import api_view
from shop.shop_users.repositories import ShopUserRepository
from shop.shop_users.serializers import ShopUserSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def shopUser(request):
    if request.method == "GET":
        return ShopUserRepository().find_by_ShopUser(request.data)
    elif request.method == "POST":
        return ShopUserSerializer().create(request.data)
    elif request.method == "PUT":
        return ShopUserSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ShopUserSerializer().delete(request.data)


@api_view(['GET'])
def shopUser_list(request):
    return ShopUserRepository().get_all(request.data)

