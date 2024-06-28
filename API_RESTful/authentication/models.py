from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('core.Project',
                                on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.username} <-> {self.project.title}"
