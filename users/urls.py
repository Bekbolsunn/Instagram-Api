from django.urls import path, include
from rest_framework import routers
from users.views import RegisterUserView


router = routers.SimpleRouter()
# router.register(r"register", RegisterUserView)

app_name = 'users'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/v1/register/', RegisterUserView.as_view(), name="instances"),
]

urlpatterns += router.urls
