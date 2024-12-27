from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


# serializer class for the User model to Create new User and get User detail
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only" : True}} # this will ensure password will not sent for get request

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# serializer class for Members
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ['full_name', 'ref_name', 'prof_pic', 'bio', 'skills', 'github', 'linkedin', 'username']
        extra_kwargs = {
            'username': {'read_only': True}  # Set 'username' field as read-only
        }