from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from newApp.serializers import StudentSerializer
from newApp.models import StudentModel

# Inherits APIViews
class TestView(APIView):
  # permission_classes = (IsAuthenticated, )

  def get(self, request, *args, **kwargs):
    qs = StudentModel.objects.all() # Get all the model objects (entries in database)
    firstStudent = qs.first() # Get first object
    serializer = StudentSerializer(firstStudent)
    return Response(serializer.data) # Returning object serializer.data when someone calls get instance method
 
  def post(self, request, *args, **kwargs):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data) 
    return Response(serializer.errors)