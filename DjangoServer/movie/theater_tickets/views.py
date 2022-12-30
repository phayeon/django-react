import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from movie.theater_tickets.number import NumberModel
from movie.theater_tickets.repositories import TheaterTicketRepository
from movie.theater_tickets.serializers import TheaterTicketSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def theaterTicket(request):
    if request.method == "GET":
        return TheaterTicketRepository().find_by_theaterTicket(request.data)
    elif request.method == "POST":
        return TheaterTicketSerializer().create(request.data)
    elif request.method == "PUT":
        return TheaterTicketSerializer().update(request.data)
    elif request.method == "PATCH":
        return None
    elif request.method == "DELETE":
        return TheaterTicketSerializer().delete(request.data)


@api_view(['GET'])
def theaterTicket_list(request):
    return TheaterTicketRepository().get_all(request.data)


@api_view(['POST'])
def number(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # json to dict
        print(f"######## GET at Here ! React ID is {data} ########")
        result = NumberModel().creat_model()
        return JsonResponse({'테스트 정확도': result})
    else:
        return JsonResponse({'result': '연결 오류'})
