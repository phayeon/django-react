from rest_framework.decorators import api_view

from shop.categories.repositories import CategoriesRepository
from shop.categories.serializers import CategoriesSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def categories(request):
    if request.method == "GET":
        return CategoriesRepository().find_by_categories(request.data)
    elif request.method == "POST":
        return CategoriesSerializer().create(request.data)
    elif request.method == "PUT":
        return CategoriesSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CategoriesSerializer().delete(request.data)


@api_view(['GET'])
def categories_list(request):
    return CategoriesRepository().get_all(request.data)

