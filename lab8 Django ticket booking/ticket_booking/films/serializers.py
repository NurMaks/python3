from rest_framework import  serializers
from .models import Film, Place, Time

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"