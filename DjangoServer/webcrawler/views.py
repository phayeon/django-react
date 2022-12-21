from django.http import JsonResponse

from webcrawler.services import ScrapService

from rest_framework.decorators import api_view


@api_view(['GET'])
def naver_movie(request):
    return JsonResponse(
        {'result': ScrapService().naver_movie_review()})

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