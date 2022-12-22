# django imports
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# from django.contrib.gis.geoip2 import GeoIP2

# local import
from .base import get_path_upload_image, validate_size_image
from config import settings


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="likes", on_delete=models.CASCADE
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Publication(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    # address = models.IntegerField()
    # likes = GenericRelation(Like)
    date_created = models.DateTimeField(auto_now_add=True)
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

    def total_likes(self):
        return self.likes.count()
