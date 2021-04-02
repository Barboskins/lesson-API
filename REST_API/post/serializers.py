from rest_framework import serializers

from post.models import Comment


# class CommentSerializer(serializers.ModelSerializer):
#     text = serializers.CharField(required=True)
#     class Meta:
#         model = Comment
#         fields = 'id', 'author', 'text'
#
#


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField(required=False)
    text = serializers.CharField(required=True)