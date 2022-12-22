from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

apipatterns = [
    path("api/v1/users/", include("users.urls")),
    path("api/v1/publications/", include("publications.urls"), name="publications"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += apipatterns

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
