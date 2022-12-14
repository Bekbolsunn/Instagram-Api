from django.urls import path
from users.views import RegisterUserView, LoginAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="Sign Up"),
    path('login/', LoginAPIView.as_view(), name="Sign In"),
    # JWT
    path('login/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
