from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, password=password **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    # Key credentials
    username = models.CharField(max_length=32, unique=True, null=False)
    password = models.CharField(max_length=256, null=False)

    # Addiotnal profile data
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)

    avatar = models.ImageField(upload_to='avatars', default="avatars/unknown.jpg", null=False)
    bio = models.TextField(max_length=256, default="", null=False)

    # Boilerplate code
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self) -> str:
        return f"User<{self.username}>"
    
    # Additional user functions
    