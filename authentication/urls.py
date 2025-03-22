from django.urls import path, include


urlpatterns = [
    path("user/", include("authentication.api.urls.user_urls")),
    path("admin/", include("authentication.api.urls.admin_urls")),
]
