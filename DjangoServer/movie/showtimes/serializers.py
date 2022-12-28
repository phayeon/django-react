from rest_framework import serializers
from movie.showtimes.models import Showtime


class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showtime
        fields = '__all__'