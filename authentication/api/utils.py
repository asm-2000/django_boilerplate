from rest_framework_simplejwt.tokens import RefreshToken
from authentication.api.models.UserModel import User
from typing import Dict, Any


def generate_token_for_user(user: User) -> Dict[str, Any]:
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
