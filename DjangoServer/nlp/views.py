import json

from django.http import JsonResponse
from rest_framework.decorators import api_view

from nlp.imdb.services import NaverMovieService
from nlp.samsung_report.services import SamsungService


@api_view(['GET'])
def report_Get(request):
    return JsonResponse({'result': SamsungService().data_analysis()})


@api_view(['POST'])
def movie_review_post(request):
    data = json.loads(request.body)
    result = NaverMovieService().process(data)
    print(f"리액트에서 받아 온 리뷰 :{data}")
    return JsonResponse({'긍정률': round(result, 2)})
