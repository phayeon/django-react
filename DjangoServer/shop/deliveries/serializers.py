from rest_framework import serializers
from shop.deliveries.models import Deliveries


class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'