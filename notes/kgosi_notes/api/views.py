from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NotesModel
from .serializers import NotesModelSerializer

# Create your views here.




@api_view(['GET'])
def getRoutes(request): # Specifies all routes in application
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes) # safe means can return more types of data not just a python dictionary

@api_view(['GET'])
def getNotes(request):
    qs_notes = NotesModel.objects.all()
    serializer = NotesModelSerializer(qs_notes, many=True)

    
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    qs_note = NotesModel.objects.get(id=pk)
    serializer = NotesModelSerializer(qs_note, many=False)
    
    return Response(serializer.data)