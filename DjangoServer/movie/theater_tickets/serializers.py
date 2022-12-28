from rest_framework import serializers
from blog.posts.models import Post
from movie.theater_tickets.models import TheaterTicket


class TheaterTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterTicket
        fields = '__all__'