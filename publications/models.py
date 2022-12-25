# django imports
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation

# local import
from .base import get_path_upload_image, validate_size_image
from users.models import CustomUser
from config import settings


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
    file = models.FileField()
    description = models.TextField(max_length=255, blank=True, null=True)
    total_likes = models.ManyToManyField(CustomUser, related_name='post_likes')
    liked_by = models.ManyToManyField(CustomUser, blank=True, related_name='liked_by')
    views = models.ManyToManyField(CustomUser, related_name='post_views')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
