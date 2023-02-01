from rest_framework import serializers
from newApp.models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = StudentModel
    fields = (
      "name", "age"
    )
  