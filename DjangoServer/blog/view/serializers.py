from rest_framework import serializers
from blog.view.models import Views


class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = '__all__'

    def create(self, validated_data):
        return Views.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Views.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass