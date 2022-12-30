from rest_framework.decorators import api_view
from blog.posts.repositories import PostRepository
from blog.posts.serializers import PostSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def post(request):
    if request.method == "GET":
        return PostRepository().find_by_post(request.data)
    elif request.method == "POST":
        return PostSerializer().create(request.data)
    elif request.method == "PUT":
        return PostSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return PostSerializer().delete(request.data)


@api_view(['GET'])
def post_list(request):
    return PostRepository().get_all(request.data)
