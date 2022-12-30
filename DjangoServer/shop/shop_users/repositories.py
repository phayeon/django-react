from rest_framework.response import Response
from shop.shop_users.models import Shop_user
from shop.shop_users.serializers import ShopUserSerializer


class ShopUserRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(ShopUserSerializer(Shop_user.objects.all(), many=True).data)

    def find_by_ShopUser(self):
        return Response(ShopUserSerializer(Shop_user.objects.all(), many=True).data)
