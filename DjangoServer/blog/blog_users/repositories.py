from django.http import JsonResponse
from rest_framework.response import Response
from blog.blog_users.models import BlogUser
from blog.blog_users.serializers import BlogUserSerializer


class UserRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(BlogUserSerializer(BlogUser.objects.all(), many=True).data)

    def find_by_email(self, param):
        return BlogUser.objects.all().filter(email=param).values()[0]

    def login(self, param):
        login_user = BlogUser.objects.get(email=param['email'])
        if login_user.password == param['password']:
            dbUser = self.find_by_email(login_user.email)
            serializer = BlogUserSerializer(dbUser, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        else:
            return JsonResponse({"data": "WRONG_PASSWORD"})

    def find_users_by_id(self, param):
        return BlogUser.objects.all().filter(blog_userid=param).values()[0]
