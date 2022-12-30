from rest_framework.decorators import api_view
from blog.view.repositories import ViewsRepository
from blog.view.serializers import ViewsSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def views(request):
    if request.method == "GET":
        return ViewsRepository().find_by_views(request.data)
    elif request.method == "POST":
        return ViewsSerializer().create(request.data)
    elif request.method == "PUT":
        return ViewsSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return ViewsSerializer().delete(request.data)


@api_view(['GET'])
def views_list(request):
    return ViewsRepository().get_all(request.data)
