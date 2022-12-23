from django.http import JsonResponse
from rest_framework.decorators import api_view

from blog.blog_users.services import UserService


@api_view(['POST'])
def login(request):
    return JsonResponse({'result ': UserService().creat_users()})

@api_view(['GET'])
def sign_up(request):
    return JsonResponse({'result ': UserService().get_users()})
