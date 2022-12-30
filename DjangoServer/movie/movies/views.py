from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from movie.movies.repositories import MoviesRepository
from movie.movies.serializers import MoviesSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def movies(request):
    if request.method == "GET":
        return MoviesRepository().find_by_movies(request.data)
    elif request.method == "POST":
        return MoviesSerializer().create(request.data)
    elif request.method == "PUT":
        return MoviesSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return MoviesSerializer().delete(request.data)


@api_view(['GET'])
def movie_list(request):
    return MoviesRepository().get_all(request.data)


@api_view(['GET'])
@parser_classes([JSONParser])
def faces(request):
    print(f'Enter Show Faces with {request}')
    return JsonResponse({'Response Test ': 'SUCCESS'})
# Create your views here.
