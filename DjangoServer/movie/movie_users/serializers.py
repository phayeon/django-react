from rest_framework import serializers
from movie.movie_users.models import Movie_user


class MovieUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_user
        fields = '__all__'

    def create(self, validated_data):
        return Movie_user.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Movie_user.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass