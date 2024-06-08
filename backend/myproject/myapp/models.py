from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    storage_path = models.CharField(max_length=255)

class File(models.Model):
    original_name = models.CharField(max_length=255)
    size = models.BigIntegerField()
    upload_date = models.DateTimeField(auto_now_add=True)
    last_download_date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    storage_path = models.CharField(max_length=255)
    special_link = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey('myapp.CustomUser', on_delete=models.CASCADE)
