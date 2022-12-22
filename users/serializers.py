# django imports
from rest_framework import serializers
from django.core.validators import FileExtensionValidator

# package imports
from phonenumber_field.serializerfields import PhoneNumberField

# local imports
from .models import CustomUser
from .services import PasswordFieldService
from .validators import phone_regex
from .choices import USER_GENDER, REGION
from .base import get_path_upload_avatar, validate_size_image


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "is_staff",
            "is_active",
            "is_superuser",
            "date_joined",
            "updated_at",
            "last_active",
        )
        read_only_fields = ("date_joined",)


class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, required=True)
    email = serializers.EmailField()
    password = PasswordFieldService(min_length=8, max_length=25, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
        ]
        read_only_fields = ("date_joined",)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = PasswordFieldService(
        max_length=25, min_length=8, write_only=True, required=True
    )


class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(
        max_length=12, validators=[phone_regex], help_text="996507100200"
    )
    nikname = serializers.CharField(max_length=25, trim_whitespace=True)
    bio = serializers.CharField(max_length=1000)
    gender = serializers.ChoiceField(USER_GENDER)
    region = serializers.ChoiceField(REGION)
    avatar = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "phone",
            "nikname",
            "bio",
            "gender",
            "region",
            "avatar",
            # "username",
            "email",
            "date_joined",
            "updated_at",
            "last_active",
        ]
        read_only_fields = ("date_joined", "last_active", "username", "email", "id")

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
