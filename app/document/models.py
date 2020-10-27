import uuid
from django.db import models
from .validators import validate_year
# Create your models here.

LANG_CHOICES = [(_, _) for _ in ('vietnamese', 'english', 'other')]
CATEGORY_CHOICES = [(_, _) for _ in ('book', 'article', 'slide', 'test')]


class Document(models.Model):
  document_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=255, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  release_year = models.IntegerField(validators=[validate_year], null=True, blank=True)
  language = models.CharField(max_length=10, choices=LANG_CHOICES, null=False, blank=False)
  category = models.CharField(max_length=7, choices=CATEGORY_CHOICES, null=False, blank=False)
  # path_to_file = models.FilePathField(null=False, auto_created=True, unique=True)
  last_update = models.DateTimeField(auto_now=True)

  class Meta:
    managed = True
    db_table = 'document'


# class Author(models.Model):
#   author_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#   name = models.CharField(max_length=255, null=False, blank=False, unique=True)
#   description = models.TextField(null=True, blank=True)
#   last_update = models.DateTimeField(auto_now=True)


# class DocumentAuthor(models.Model):
#   document = models.ForeignKey(Document, models.DO_NOTHING, null=False)
#   author = models.ForeignKey(Author, models.DO_NOTHING, null=False)

#   class Meta:
#     unique_together = (('document', 'author'),)