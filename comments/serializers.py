from rest_framework import serializers
from . import models


class ReplySerializer(serializers.ModelSerializer):
    comment_name = serializers.CharField(source='comment.title_for_comment',read_only=True)
    class Meta:
        model = models.Reply
        fields = ('comment','reply_text','created_at','comment_name')
        read_only_fields=('created_at',)

class CommentsSerializer(serializers.ModelSerializer):
    reply = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='reply_text'
     )
    reply = serializers.StringRelatedField(read_only=True,many=True)
    date_created = serializers.DateField(read_only=True)

    class Meta:
        model = models.Comments
        fields = ['title_for_comment','text','reply','date_created']
