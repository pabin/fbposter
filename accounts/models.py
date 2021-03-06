from django.core.exceptions import ValidationError

from django.db import models
from django.contrib.auth.models import User


class FacebookPageID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    page_id = models.CharField(max_length=128)
    added_on = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class FacebookAccessToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.added_on)
