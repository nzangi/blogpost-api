from django.shortcuts import render
from rest_framework.response import Response
from blog.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.db import transaction
from rest_framework.decorators import permission_classes,api_view
from blog.models import Post
from django.contrib.auth.models import User
from rest_framework import status
# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def view_posts(request):
    if request.method =='GET':
        posts = Post.objects.all()
        postSerializer = PostSerializer(posts,many=True)
        return Response({'data':postSerializer.data},status=status.HTTP_200_OK)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_post(request):
    if request.method == 'POST':
        postSerializer = PostSerializer(data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data,status=status.HTTP_201_CREATED)


 
