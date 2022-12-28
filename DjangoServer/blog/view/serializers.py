from rest_framework import serializers
from blog.view.models import Views


class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = '__all__'