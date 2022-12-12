from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# from django.core.validators import FileExtensionValidator

from phonenumber_field.modelfields import PhoneNumberField


from .managers import UserManager
# from .base import get_path_upload_avatar, validate_size_image


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Sign Up"""

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(db_index=True)

    """Sign In"""
    phone = PhoneNumberField(blank=True, null=True, help_text='Contact phone number')
    nikname = models.CharField(max_length=35)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    # avatar = models.ImageField(
    #     upload_to=get_path_upload_avatar,
    #     blank=True,
    #     null=True,
    #     validators=[
    #         FileExtensionValidator(allowed_extensions=["jpg"]),
    #         validate_size_image,
    #     ],
    # )

    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    is_superuser = models.BooleanField("Cуперпользователь", default=False)
    updated_at = models.DateTimeField("Обновлено в", auto_now=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)
    last_active = models.DateTimeField(
        "Дата последой активности", null=True, blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    def __str__(self):
        return self.username

    # @property
    # def is_authenticated(self):
    #     """Пользователь аутентифицирован"""
    #     return True

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


# class Follower(models.Model):
#     """Модель подписчиков"""
#
#     user = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="Владелец"
#     )
#     subscriber = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="Подписчики"
#     )
#
#     def __str__(self):
#         return f"{self.subscriber} подписан(а) на {self.user}"
#
#
# class SocialLink(models.Model):
#     """Модель для соц ссылок"""
#
#     user = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE, related_name="Ссылка для сети+"
#     )
#     link = models.URLField(max_length=400)
#
#     def __str__(self):
#         return f"{self.user}"
