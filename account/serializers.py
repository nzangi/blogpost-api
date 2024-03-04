from account.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    '''Profile User Fields'''
    class Meta:
        
        # Get the profile_user currently Logged In User

        fields = ['title','description','image']
