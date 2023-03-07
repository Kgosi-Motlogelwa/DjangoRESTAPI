from rest_framework.response import Response
from .models import NotesModel
from .serializers import NotesModelSerializer

def getAllNotes(request):
    qs_notes = NotesModel.objects.all().order_by("-updated")
    serializer = NotesModelSerializer(qs_notes, many=True)
    return Response(serializer.data)

def getOneNote(request, pk):
    qs_note = NotesModel.objects.get(id=pk)
    serializer = NotesModelSerializer(qs_note, many=False)
    return Response(serializer.data)

def createNote(request): 
    data = request.data
    note = NotesModel.objects.create(
        body=data['body']
    )
    serializer = NotesModelSerializer(note, many=False)
    return Response(serializer.data)

def updateNote(request, pk):
    data = request.data # DRF allows us to get
    noteToUpdate = NotesModel.objects.get(id=pk)
    serializer = NotesModelSerializer(instance=noteToUpdate, data = data)
        
    if serializer.is_valid():  
        serializer.save()
        return Response(serializer.data)
    
def deleteNote(request, pk):
    note = NotesModel.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted!')
 
