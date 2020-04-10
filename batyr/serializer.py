from rest_framework import serializers

from batyr.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'category_comment',
            'comment_txt',
        ]
