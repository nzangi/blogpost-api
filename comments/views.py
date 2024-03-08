from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from comments.models import Comments
from blog.serializers import PostSerializer
from blog.models import Post
from comments.serializers import CommentSerializer
from rest_framework.decorators import permission_classes,api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def view_all_comments(request,post_id):
    try:
        post_posted = Post.objects.get(pk=post_id)
        all_comments = Comments.objects.filter(commented_post=post_posted)
    except post_posted.DoesNotExist:
        return Response({'message':'There is no such post'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        post_comments = CommentSerializer(all_comments,many=True)
        postSerializer = PostSerializer(post_posted)
        return Response({'post':postSerializer.data,'comments':post_comments.data},status=status.HTTP_200_OK)
    return Response({'errors':post_comments.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def comment_on_post(request,post_id):
    pass
