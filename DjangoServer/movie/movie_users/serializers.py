from rest_framework import serializers
from movie.movie_users.models import Movie_user


class Movie_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_user
        fields = '__all__'