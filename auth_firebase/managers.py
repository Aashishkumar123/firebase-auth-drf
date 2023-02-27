from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class FirebaseManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, useruid, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not useruid:
            raise ValueError(_("The UserUID must be set"))
        user = self.model(useruid=useruid, **extra_fields)
        user.save()
        return user

    def create_superuser(self, useruid, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(useruid, **extra_fields)
