from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from auth_firebase.managers import FirebaseManager


class FirebaseUser(AbstractUser):
   
    password = None
    useruid = models.CharField(_("User UID"), max_length=100, unique=True)
   
    USERNAME_FIELD = "useruid"
    REQUIRED_FIELDS = []
    
    objects = FirebaseManager()

    def __str__(self):
        return self.useruid
