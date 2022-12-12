from rest_framework import serializers
from .models import CustomUser
from .services import PasswordField
from phonenumber_field.serializerfields import PhoneNumberField


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
        )
        read_only_fields = ("date_joined",)


class ProfileUpdateSerializers(serializers.Serializer):
    nikname = serializers.CharField(max_length=25)
    bio = serializers.CharField(max_length=1000)
    phone = PhoneNumberField(help_text='Contact phone number')
    pass


class RegisterSerializers(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField()
    password = PasswordField(min_length=8, max_length=25, write_only=True)

    # def create(self, validate_data):
    #     return CustomUser.objects.create_user(
    #         username=validate_data["username"],
    #         email=validate_data["email"],
    #     )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password",
        ]
        read_only_fields = ("date_joined",)

# class LoginResponseSerializer(serializers.Serializer):
#     user = UserSerializer()
#     refresh = serializers.CharField()
#     access = serializers.CharField()
