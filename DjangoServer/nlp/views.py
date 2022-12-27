from django.http import JsonResponse
from rest_framework.decorators import api_view

from nlp.samsung_report.services import SamsungService


@api_view(['GET'])
def report_Get(request):
    return JsonResponse({'result': SamsungService().data_analysis()})

