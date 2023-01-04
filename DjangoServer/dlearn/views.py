import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
import tensorflow as tf

from dlearn.aitrader.services import AITraderService
from dlearn.fashion.fashion_service import FashionService
from dlearn.iris.iris_model import IrisModel
from dlearn.iris.irls_service import IrisService
from dlearn.stroke.stroke import StrokeService


@api_view(['GET', 'POST'])
def fashion(request):
    if request.method == 'GET':
        print("#####", request.GET['get_num'])
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['get_num']))})
    elif request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## GET at Here ! React ID is {int(data)} ########")
        result = FashionService().service_model(int(data))
        return JsonResponse({'result': result})


@api_view(['GET'])
def stroke(request):
    print(f'Stroke Check {request}')
    StrokeService().hook()
    return JsonResponse({'Response Test ': 'SUCCESS'})


@api_view(['GET'])
def iris_Get(request):
    IrisModel().spec()
    return JsonResponse({'Response Test ': 'SUCCESS'})


@api_view(['POST'])
def iris_Post(request):
    iris_info = json.loads(request.body)
    sl = tf.constant(float(iris_info['sl']))
    sw = tf.constant(float(iris_info['sw']))
    pl = tf.constant(float(iris_info['pl']))
    pw = tf.constant(float(iris_info['pw']))
    req = [sl, sw, pl, pw]
    t = IrisService()
    print(f'리액트에서 받아 온 데이터 : {request}')
    print(f'꽃받침 길이 : {sl}')
    print(f'꽃받침 넓이 : {sw}')
    print(f'꽃잎 길이 : {pl}')
    print(f'꽃잎 넓이 : {pw}')
    return JsonResponse({'예상되는 꽃의 이름 ': t.service_model(req)})

@api_view(['POST'])
def aiTrader_Post(request):
    return JsonResponse({'result': AITraderService().hook(int(request.data))})

