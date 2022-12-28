from rest_framework import serializers
from movie.theaters.models import Theater


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = '__all__'