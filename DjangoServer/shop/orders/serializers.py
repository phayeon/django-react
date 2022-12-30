from rest_framework import serializers
from shop.orders.models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Orders.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass