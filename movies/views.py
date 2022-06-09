import json

from django.http import JsonResponse
from django.views import View

from .models import Actor, Movie, ActorsMovies


class ActorView(View):
    """
    목적: 모든 배우들의 정보를 client에 전달

    1. last_name
    2. first_name
    3. date_of_birth
    4. movies

    """

    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            movies = actor.actors.all()

            results.append(
                {
                    "1. last_name" : actor.last_name,
                    "2. first_name" : actor.first_name,
                    "3. date_of_birth" : actor.date_of_birth,
                    "4. movies" : [movie.title for movie in movies]
                }
            )
        return JsonResponse({"results":results}, status=200)

class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []

        for movie in movies:
            actors = movie.actors.all()
            results.append(
                {
                    "1. title" : movie.title,
                    "2. release_date" : movie.release_date,
                    "3. running_time" : movie.running_time,
                    "4. actors" : [actor.last_name for actor in actors]
                }
            )

        return JsonResponse({"results" : results}, status=200)
