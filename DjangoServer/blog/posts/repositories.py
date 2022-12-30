from django.http import JsonResponse
from rest_framework.response import Response
from blog.posts.models import Post
from blog.posts.serializers import PostSerializer


class PostRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(PostSerializer(Post.objects.all(), many=True).data)

    def find_by_post(self):
        return Response(PostSerializer(Post.objects.all(), many=True).data)
