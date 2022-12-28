from rest_framework import serializers
from movie.cienmas.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'