from rest_framework import serializers
from movie.movies.models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

    def create(self, validated_data):
        return Movies.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Movies.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass