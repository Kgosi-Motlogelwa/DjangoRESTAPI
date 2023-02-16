from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from newApp.serializers import StudentSerializer
from newApp.models import StudentModel

# Inherits APIViews
class TestView(APIView):
   def get(self, request, *args, **kwargs):
     data = {
       "username": "admin",
       "years_active": 10,
     }
     # Returning object data when someone calls get instance method
     return Response(data)
   def post(self, request, *args, **kwargs):
     serializer = StudentSerializer(data=request.data)
     print("serializer: ", serializer)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)

     return Response(serializer.errors)



