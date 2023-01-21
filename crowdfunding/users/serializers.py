from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    company = serializers.CharField(max_length=200)
    image = serializers.URLField()
    bio = serializers.CharField(max_length=None)

    def create (self, validated_data):
            return CustomUser.objects.create_user(**validated_data)

            