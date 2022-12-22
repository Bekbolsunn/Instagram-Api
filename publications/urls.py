from django.urls import path, include
from rest_framework import routers
from .views import PublicationView

app_name = 'publications'

router = routers.SimpleRouter()
router.register("publicate", PublicationView)

urlpatterns = [
    path('', include(router.urls), name='crud-publicate'),
]
urlpatterns += router.urls
