from rest_framework import serializers
from shop.shop_users.models import Shop_user


class Shop_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop_user
        fields = '__all__'