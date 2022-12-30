from rest_framework import serializers
from shop.categories.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

    def create(self, validated_data):
        return Categories.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Categories.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass