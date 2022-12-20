import json

from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from dlearn.iris.iris_model import IrisModel
from dlearn.iris.irls_service import IrisService
from movie.theater_tickets.number import NumberModel


@api_view(['POST'])
def number(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## GET at Here ! React ID is {data} ########")
        result = NumberModel().creat_model()
        return JsonResponse({'테스트 정확도': result})
    else:
        return JsonResponse({'result': '연결 오류'})
