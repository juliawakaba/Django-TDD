"""Database models"""
from django.db import models
from django.contrib.auth.models import AbstarctBaseUser, BaseUserManager, PermissionMixin


class UserManager(BaseUserManager):
    """Manager for users"""
    def create_user(self, email, password=None, **extra_fields):
        """Create, svae and return a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 

class User(AbstarctBaseUser, PermissionMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email