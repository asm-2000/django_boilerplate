from rest_framework import serializers
from authentication.api.models.UserModel import User, UserDetails
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]
        required_fields = ["email", "username", "password"]


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ["first_name", "last_name", "profile_image_url", "date_of_birth", "country"]


class UserCredentialSerializer(serializers.ModelSerializer):
    user_details = UserDetailsSerializer()
    class Meta:
        model = User
        fields = ["id", "email", "username", "user_details"]


class UserLoginCredentialSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
