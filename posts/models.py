# django imports
from django.db import models
from django.core.validators import FileExtensionValidator
# from django.contrib.gis.geoip2 import GeoIP2

# local import
from .base import get_path_upload_image, validate_size_image
from users.models import CustomUser


class Publication(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    # address = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, blank=True)
    image = models.ImageField(
        upload_to=get_path_upload_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg"]),
            validate_size_image,
        ],
    )

    def __str__(self):
        return self.title
