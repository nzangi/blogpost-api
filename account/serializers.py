from account.models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileSerializer(serializers.ModelSerializer):
    '''Profile User Fields'''
    # profile_user = UserSerializer()
    class Meta:
        model = Profile
        # Get the profile_user currently Logged In User
        fields = ['title','description','image']
