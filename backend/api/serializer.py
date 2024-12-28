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


# serializer class for Projects
class ProjectSerializer(serializers.ModelSerializer):
    # spesify the project_pics field as a list of images
    project_pics = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=True),required=False)

    class Meta:
        model = Projects
        fields = ['title', 'description', 'project_pics', 'cover_pic', 'demo_link']


# serializer class for Reviews
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['review', 'rating', 'date']
        extra_kwargs = {
            'date': {'read_only': True},
            'project': {'read_only': True}
        }