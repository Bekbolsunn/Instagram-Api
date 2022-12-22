from django.urls import path, include
from .views import (
    RegisterUserView,
    LoginAPIView,
    ProfileViewSet,
)

from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

ROUTER = SimpleRouter()
ROUTER.register(r"profile", ProfileViewSet, "profile")

app_name = "users"

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="Sign Up"),
    path("login/", LoginAPIView.as_view(), name="Sign In"),
    # JWT
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(ROUTER.urls)),
]
