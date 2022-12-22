from django.urls import path, include
from rest_framework import routers
from .views import PublicationView

app_name = "publications"

ROUTER = routers.SimpleRouter()
ROUTER.register("publicate", PublicationView, "publicate")

urlpatterns = [
    path("", include(ROUTER.urls)),
]
urlpatterns += ROUTER.urls
