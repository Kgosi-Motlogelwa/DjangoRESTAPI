from django.shortcuts import render
from .models import MovieModel
from django.http import JsonResponse

# Create your views here. Choosing to use function based views
def movie_list(request):
    qs_MoviesAll = MovieModel.objects.all()
    # .values returns qs as python dictionary <QuerySet [{'id': 1, 'name': 'Python vs Typescript', 'desription': 'The original', 'active': True}, {'id': 2, 'name': 'Typescript - The Past', 'desription': 'The old man', 'active': True}]>
    data = {'movies': list(qs_MoviesAll.values())}
     
    return JsonResponse(data)

def movie_details(request, pk):
    qs_Movie = MovieModel.objects.get(pk=pk)
    print(qs_Movie)
    data = {
        'name': qs_Movie.name,
        'description': qs_Movie.description,
        'active': qs_Movie.active
    }
    return JsonResponse(data)

    