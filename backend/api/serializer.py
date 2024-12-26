from rest_framework import serializers
from django.contrib.auth.models import User


# serializer class for the User model to Create new User and get User detail
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only" : True}} # this will ensure password will not sent for get request

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user