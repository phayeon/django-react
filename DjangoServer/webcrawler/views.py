from django.http import JsonResponse
from rest_framework.decorators import api_view
from webcrawler.services import ScrapService


@api_view(['GET'])
def naver_movie(request):
    if request.method == 'GET':
        return JsonResponse(
            {'영화': ScrapService().naver_movie_review()})
    else:
        return JsonResponse({'result': 'error'})

'''
class ScrapController(object):
    @staticmethod
    def Menu_0(*params):
        print(params[0])

    @staticmethod
    def Menu_1(*params):
        print(params[0])
        ScrapService().bugs_music(params[1])

    @staticmethod
    def Menu_2(*params):
        print(params[0])
        ScrapService().melon_music(params[1])
'''