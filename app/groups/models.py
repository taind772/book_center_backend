import uuid
import unicodedata
from django.db import models


class AbstractGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    last_update = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    @classmethod
    def normalize_name(cls, name: str):
        name = unicodedata.normalize('NFKC', name.strip())
        return name


class Author(AbstractGroup):

    class Meta:
        db_table = 'author'


# class Topic(AbstractGroup):
#
#     class Meta:
#         db_table = 'topic'


class Label(AbstractGroup):

    class Meta:
        db_table = 'label'


class Publisher(AbstractGroup):

    class Meta:
        db_table = 'publisher'
