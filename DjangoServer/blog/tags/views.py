from rest_framework.decorators import api_view

from blog.tags.repositories import TagRepository
from blog.tags.serializers import TagSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def tags(request):
    if request.method == "GET":
        return TagRepository().find_by_tag(request.data)
    elif request.method == "POST":
        return TagSerializer().create(request.data)
    elif request.method == "PUT":
        return TagSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TagSerializer().delete(request.data)


@api_view(['GET'])
def tags_list(request):
    return TagRepository().get_all(request.data)
