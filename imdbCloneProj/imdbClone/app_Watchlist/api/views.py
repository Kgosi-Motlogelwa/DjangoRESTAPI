from app_Watchlist.models import MovieModel
from .serializers import MovieModelSerializer
from rest_framework.response import Response

def movie_list(request):
    movies = MovieModel.objects.all()
    print(movies)
    serialized_movies = MovieModelSerializer(movies)
    print("serialized_movies: ", serialized_movies)
    return Response(serialized_movies.data)


def movie_details(request):
    movie = MovieModel.objects.get(pk=pk)
    serialized_movie = MovieModelSerializer(movie)
    return Response(serialized_movie.data)


    