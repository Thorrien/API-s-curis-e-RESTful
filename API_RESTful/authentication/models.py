from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField()
    can_be_contacted = models.BooleanField(default=False)
    can_be_shared = models.BooleanField(default=False)


class Contributor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

