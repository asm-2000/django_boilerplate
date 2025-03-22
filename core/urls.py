from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("backend/api/admin/", admin.site.urls),
    path("backend/api/authentication/", include("authentication.urls")),
    path(
        "backend/api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("backend/api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "backend/api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
