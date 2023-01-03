# django imports
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

# local import
from .base import get_path_upload_image, validate_size_image
from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(
        upload_to=get_path_upload_image,
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg"]),
            validate_size_image,
        ],
    )
    description = models.TextField(max_length=255, blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
