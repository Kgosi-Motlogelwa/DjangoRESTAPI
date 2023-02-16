from rest_framework import serializers
from app_Watchlist.models import MovieModel

class MovieModelSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField()
    # description = serializers.CharField() 
    # active = serializers.BooleanField()
    
    class Meta:
        model = MovieModel
        fields = ("name", "description", "active")
