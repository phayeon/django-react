from rest_framework.decorators import api_view
from blog.comment.repositories import CommentRepository
from blog.comment.serializers import CommentSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def comment(request):
    if request.method == "GET":
        return CommentRepository().find_by_comment(request.data)
    elif request.method == "POST":
        return CommentSerializer().create(request.data)
    elif request.method == "PUT":
        return CommentSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return CommentSerializer().delete(request.data)


@api_view(['GET'])
def comment_list(request):
    return CommentRepository().get_all(request.data)
