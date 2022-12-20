import json
from django.http import JsonResponse
from rest_framework.decorators import api_view

from dlearn.fashion.fashion_service import FashionService


@api_view(['GET', 'POST'])
def fashion(request):
    if request.method == 'GET':
        return JsonResponse(
            {'result': FashionService().service_model(int(request.GET['get_num']))})
    elif request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## GET at Here ! React ID is {int(data)} ########")
        result = FashionService().service_model(int(data))
        return JsonResponse({'result': result})
