from django.http import JsonResponse
from rest_framework.response import Response

from blog.comment.models import Comment
from blog.comment.serializers import CommentSerializer


class CommentRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(CommentSerializer(Comment.objects.all(), many=True).data)

    def find_by_comment(self):
        return Response(CommentSerializer(Comment.objects.all(), many=True).data)
