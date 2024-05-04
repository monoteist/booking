from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('tenant', 'Tenant'),
        ('owner', 'Owner'),
    )
    user_type = models.CharField(max_length=6, choices=USER_TYPE_CHOICES)
