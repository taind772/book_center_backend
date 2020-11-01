import uuid
from django.db import models


class Author(models.Model):
    author_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.name
