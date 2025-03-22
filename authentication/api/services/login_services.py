from authentication.api.utils import generate_token_for_user
from authentication.api.models.UserModel import User
from authentication.api.serializers import UserCredentialSerializer
from rest_framework import status
from django.contrib.auth.hashers import check_password
from global_utils.service_return import service_return


def login_user(user_login_credentials):
    try:
        username = user_login_credentials.validated_data.get("username")
        password = user_login_credentials.validated_data.get("password")
        user = User.objects.filter(username=username).first()
        if not user:
            return service_return(
                message="User not found",
                status=status.HTTP_404_NOT_FOUND,
                data=None,
                error=None,
            )
        if check_password(password, user.password):
            token_obj = generate_token_for_user(user=user)
            user_data = UserCredentialSerializer(user).data
            return_data = {
                "user_credentials": user_data,
                "access": token_obj.get("access"),
                "refresh": token_obj.get("refresh"),
            }
            return service_return(
                message="Logged in successfully",
                status=status.HTTP_200_OK,
                data=return_data,
                error=None,
            )
        else:
            return service_return(
                message="Invalid credentials",
                status=status.HTTP_401_UNAUTHORIZED,
                data=None,
                error=None,
            )
    except Exception as e:
        return service_return(
            message="Could not login user",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            data=None,
            error=str(e),
        )
