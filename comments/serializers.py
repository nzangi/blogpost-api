from rest_framework import serializers
from comments.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    comment_author = serializers.SerializerMethodField()

    def get_comment_author(self, user):
        return user.comment_author.username
        
    class Meta:
        model = Comments
        fields = ['comment_text','comment_author','commented_date']