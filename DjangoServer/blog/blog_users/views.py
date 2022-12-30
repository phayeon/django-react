from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from blog.blog_users.repositories import UserRepository
from blog.blog_users.serializers import BlogUserSerializer
from blog.blog_users.services import UserService


@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def blog_user(request):
    if request.method == "POST":
        return BlogUserSerializer().create(request.data)
    elif request.method == "GET":
        return UserRepository().find_by_id(request.data)
    elif request.method == "PUT":
        return BlogUserSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return BlogUserSerializer().delete(request.data)


@api_view(['GET'])
def blog_user_list(request):
    return UserRepository().get_all()


@api_view(['GET'])
def user_create(request):
    return JsonResponse({'result ': UserService().creat_users()})


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    return UserRepository().login(request.data)
