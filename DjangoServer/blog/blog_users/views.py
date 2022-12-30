from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from blog.blog_users.repositories import UserRepository
from blog.blog_users.serializers import BlogUserSerializer
from blog.blog_users.services import UserService


@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def blog_user(request):
    if request.method == "POST":
        new_user = request.data
        print(f'react에서 등록한 신규 사용자 {new_user}')
        serializer = BlogUserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"result": "SUCCESS"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        return Response(UserRepository().find_by_email(request.data['email']))
    elif request.method == "PATCH":
        return None
    elif request.method == "PUT":
        repo = UserRepository()
        modify_user = repo.find_by_email(request.data['email'])
        db_user = repo.find_users_by_id(modify_user.blog_userid)
        serializer = BlogUserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user, db_user)
            return JsonResponse({'result': 'SUCCESS'})
    elif request.method == "DELETE":
        repo = UserRepository()
        delete_user = repo.find_by_email(request.data['email'])
        db_user = repo.find_users_by_id(delete_user.blog_userid)
        db_user.delete()
        return JsonResponse({'result': 'SUCCESS'})


@api_view(['GET'])
def blog_user_list(request):
    return UserRepository().get_all()


@api_view(['GET'])
def find_user_id(request):
    return UserRepository().find_users_by_id(request.data['blog_userid'])


@api_view(['GET'])
def user_create(request):
    return JsonResponse({'result ': UserService().creat_users()})


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    return UserRepository().login(request.data)
