from dataclasses import fields
from .models import CustomUser,UserProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomUser
        fields = ("id","email","last_login","is_staff","created_at","updated_at")


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = UserProfile
        fields = "__all__"