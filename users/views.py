from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from users.serializers import RegisterUserSerializer,LoginUserSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([])
de