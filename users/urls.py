from django.urls import path, include
from rest_framework import routers
from users.views import RegisterUserView, LoginAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.SimpleRouter()
# router.register(r"register", RegisterUserView)

app_name = 'users'

urlpatterns = [
    path('router/', include(router.urls)),
    path('register/', RegisterUserView.as_view(), name="Sign Up"),
    path('login/', LoginAPIView.as_view(), name="Sign In"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
