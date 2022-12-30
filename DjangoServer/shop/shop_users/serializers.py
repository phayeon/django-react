from rest_framework import serializers
from shop.shop_users.models import Shop_user


class ShopUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_user
        fields = '__all__'

    def create(self, validated_data):
        return Shop_user.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Shop_user.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass