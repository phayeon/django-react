from django.http import JsonResponse
from rest_framework.response import Response
from blog.view.models import Views
from blog.view.serializers import ViewsSerializer


class ViewsRepository(object):
    def __init__(self):
        pass

    def get_all(self):
        return Response(ViewsSerializer(Views.objects.all(), many=True).data)

    def find_by_views(self):
        return Response(ViewsSerializer(Views.objects.all(), many=True).data)
