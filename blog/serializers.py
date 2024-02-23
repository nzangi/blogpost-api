from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']  # Assuming 'username' is the field representing the author's name


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, user):
        return user.author.username
    
    class Meta:
        model = Post
        fields =['title','content','date_posted','author']

    
