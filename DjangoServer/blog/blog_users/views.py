from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from blog.blog_users.models import BlogUser
from blog.blog_users.serializers import BlogUserSerializer
from blog.blog_users.services import UserService


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        print(f'로그인 정보: {request.data}')
        login_info = request.data
        login_user = BlogUser.objects.get(email=login_info['email'])
        print(f'해당 email을 가진 user: {login_user}')
        if login_user.password == login_info['password']:
            dbUser = BlogUser.objects.all().filter(nickname=login_user.nickname).values()[0]
            print(f" DBUser is {dbUser}")
            serializer = BlogUserSerializer(dbUser, many=False)
            print('로그인 성공')
            return JsonResponse(data=serializer.data, safe=False)
    except:
        return Response("LOGIN FAIL")


@api_view(['GET'])
def user_list(request):
    if request.method == "GET":
        serializer = BlogUserSerializer(BlogUser.objects.all(), many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_create(request):
    return JsonResponse({'result ': UserService().creat_users()})



if __name__ == '__main__':
    n = input('name')
    a = input('age')
    u = BlogUser(n, a)
    print(u.n)
    print(u.a)