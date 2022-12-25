from django.urls import path, include
from rest_framework import routers
from .views import PostView

app_name = "publications"

ROUTER = routers.SimpleRouter()
ROUTER.register("post", PostView, "post")

urlpatterns = [
    path("", include(ROUTER.urls)),
]
urlpatterns += ROUTER.urls
