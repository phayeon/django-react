from rest_framework import serializers
from blog.comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, valicated_data):
        Comment.objects.filter(pk=instance.id).update(**valicated_data)

    def delete(self, instance, valicated_data):
        pass