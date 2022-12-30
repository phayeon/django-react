from rest_framework import serializers
from shop.deliveries.models import Deliveries


class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'

    def create(self, validated_data):
        return Deliveries.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Deliveries.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass