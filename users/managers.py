from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not username:
            raise ValueError("Users must have a username.")
        if not email:
            raise ValueError("Users must have an email address.")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password):
        return self._create_user(email, username, password)

    def create_superuser(self, email, username, password):
        return self._create_user(
            email, username, password, is_staff=True, is_superuser=True
        )
