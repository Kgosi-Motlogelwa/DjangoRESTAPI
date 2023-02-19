from rest_framework.serializers import ModelSerializer
from .models import NotesModel

class NotesModelSerializer(ModelSerializer):
    class Meta:
        model = NotesModel
        fields = '__all__'