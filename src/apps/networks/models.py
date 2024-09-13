from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db import models
import uuid

from apps.accounts.models import User

# Create your models here.
class Follow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    uuid = models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False)
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'follower') 

    def clean(self):
        if self.user == self.follower:
            raise ValidationError("You cannot follow yourself.")

    def save(self, *args, **kwargs):
        self.clean()  # Ensure that clean method is called
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"