from rest_framework.generics import GenericAPIView
from authentication.api import serializers
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import status
from authentication.api.services import registration_services, login_services
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from global_utils.global_return.api_return import api_response


class UserRegisterView(GenericAPIView):
    serializer_class = serializers.UserRegisterSerializer
    throttle_classes = [AnonRateThrottle]

    @extend_schema(tags=["Authentication"])
    def post(self, request, *args, **kwargs):
        request_obj = self.serializer_class(data=request.data)
        if not request_obj.is_valid():
            return api_response(
                message="Invalid data",
                error=request_obj.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        result_obj = registration_services.register_user(request_obj)
        return api_response(
            message=result_obj.get("message"),
            data=result_obj.get("data"),
            status=result_obj.get("status"),
            error=result_obj.get("error"),
        )


class UserLoginView(GenericAPIView):
    serializer_class = serializers.UserLoginCredentialSerializer
    throttle_classes = [AnonRateThrottle]

    @extend_schema(tags=["Authentication"])
    def post(self, request, *args, **kwargs):
        request_obj = self.serializer_class(data=request.data)
        if not request_obj.is_valid():
            return api_response(
                message="Invalid data",
                error=request_obj.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        result_obj = login_services.login_user(request_obj)
        return api_response(
            message=result_obj.get("message"),
            data=result_obj.get("data"),
            status=result_obj.get("status"),
        )


class RefreshAccessTokenView(GenericAPIView):
    serializer_class = TokenRefreshSerializer
    throttle_classes = [UserRateThrottle]

    @extend_schema(tags=["Authentication"])
    def post(self, request, *args, **kwargs):
        request_obj = self.serializer_class(data=request.data)
        try:
            request_obj.is_valid(raise_exception=True)
        except Exception as e:
            return api_response(
                message="Invalid data",
                error=str(e),
                status=status.HTTP_400_BAD_REQUEST,
            )
        new_token = request_obj.validated_data
        return api_response(
            message="Success",
            data=new_token,
            status=status.HTTP_200_OK,
        )


class UserDetailsView(GenericAPIView):
    serializer_class = serializers.UserDetailsSerializer
    throttle_classes = [UserRateThrottle]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["Authentication"])
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("user_id")
        result_obj = registration_services.get_user_credentials(user_id)
        return api_response(
            message=result_obj.get("message"),
            data=result_obj.get("data"),
            status=result_obj.get("status"),
            error=result_obj.get("error"),
        )

    @extend_schema(tags=["Authentication"])
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get("user_id")
        if user_id != request.user.id:
            return api_response(
                message="Permission denied",
                status=status.HTTP_403_FORBIDDEN,
            )
        result_obj = registration_services.update_user_details(
            user_id=user_id, user_details=request.data
        )
        return api_response(
            message=result_obj.get("message"),
            data=result_obj.get("data"),
            status=result_obj.get("status"),
            error=result_obj.get("error"),
        )

    @extend_schema(tags=["Authentication"])
    def post(self, request, *args, **kwargs):
        user_id = kwargs.get("user_id")
        if user_id != request.user.id:
            return api_response(
                message="Permission denied",
                status=status.HTTP_403_FORBIDDEN,
            )
        result_obj = registration_services.update_user_details(
            user_id=user_id, user_details=request.data
        )
        return api_response(
            message=result_obj.get("message"),
            data=result_obj.get("data"),
            status=result_obj.get("status"),
            error=result_obj.get("error"),
        )