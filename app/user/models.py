import uuid
from django.db import models

# Create your models here.

class User(models.Model):
  user_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  username = models.CharField(unique=True, max_length=40)
  email = models.EmailField(unique=True, max_length=255)
  hash_pass = models.CharField(max_length=255)
  last_update = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'users'