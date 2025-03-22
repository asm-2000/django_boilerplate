from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from rest_framework import status
from authentication.api.models.UserModel import User, UserDetails
from authentication.api.serializers import (
    UserCredentialSerializer,
    UserDetailsSerializer,
)
from authentication.api.utils import generate_token_for_user
from global_utils.service_return import service_return


def register_user(user_credentials):
    try:
        exist_user = User.objects.filter(
            email=user_credentials.validated_data.get("email")
        ).first()
        if exist_user:
            return service_return(
                message="User already exists for the provided email",
                status=status.HTTP_400_BAD_REQUEST,
            )
        validate_password(user_credentials.validated_data.get("password"))
        user_credentials.validated_data["password"] = make_password(
            user_credentials.validated_data["password"]
        )
        user_obj = user_credentials.save()
        user = User.objects.filter(id=user_obj.id).first()
        if not user:
            return service_return(
                message="Could not register user",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        token_obj = generate_token_for_user(user_credentials.instance)
        user_data = UserCredentialSerializer(user).data
        return_data = {
            "user_credentials": user_data,
            "access": token_obj.get("access"),
            "refresh": token_obj.get("refresh"),
        }
        return service_return(
            message="User registered successfully",
            status=status.HTTP_201_CREATED,
            data=return_data,
            error=None,
        )
    except Exception as e:
        return service_return(
            message="Could not register user",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=str(e),
        )


def get_user_credentials(user_id):
    try:
        user = User.objects.filter(id=user_id).first()
        if not user:
            return service_return(
                message="User not found",
                status=status.HTTP_404_NOT_FOUND,
            )
        user_data = UserCredentialSerializer(user).data
        return service_return(
            message="User credentials fetched successfully",
            status=status.HTTP_200_OK,
            data=user_data,
        )
    except Exception as e:
        return service_return(
            message="Could not fetch user credentials",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=str(e),
        )


def update_user_details(user_id, user_details):
    try:
        user_exists = User.objects.filter(id=user_id).first()
        if not user_exists:
            return service_return(
                message="User not found",
                status=status.HTTP_404_NOT_FOUND,
            )
        user_details_obj = UserDetails.objects.filter(user_id=user_id).first()
        user_details_serializer = UserDetailsSerializer(
            user_details_obj, data=user_details, partial=True
        )
        if not user_details_serializer.is_valid():
            return service_return(
                message="Invalid data",
                status=status.HTTP_400_BAD_REQUEST,
                error=user_details_serializer.errors,
            )
        user_details_serializer.save(user_id=user_id)
        updated_data = UserDetailsSerializer(user_exists.user_details).data
        return service_return(
            message="User credentials updated successfully",
            status=status.HTTP_200_OK,
            data=updated_data,
        )
    except Exception as e:
        return service_return(
            message="Could not update user credentials",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error=str(e),
        )
