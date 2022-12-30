from rest_framework.response import Response

from shop.categories.models import Categories
from shop.categories.serializers import CategoriesSerializer


class CategoriesRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(CategoriesSerializer(Categories.objects.all(), many=True).data)

    def find_by_categories(self):
        return Response(CategoriesSerializer(Categories.objects.all(), many=True).data)
