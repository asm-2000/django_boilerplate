from django.urls import path
from authentication.api.views import user_views

urlpatterns = [
    path(
        "register_user/", user_views.UserRegisterView.as_view(), name="UserRegisterView"
    ),
    path("login_user/", user_views.UserLoginView.as_view(), name="UserLoginView"),
    path("refresh_access_token/", user_views.RefreshAccessTokenView.as_view(), name="RefreshAccessTokenView"),
    path("user_details/<uuid:user_id>/", user_views.UserDetailsView.as_view(), name="UserDetailsView"),
]
