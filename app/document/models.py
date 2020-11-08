import uuid
from django.db import models
from .validators import validate_year


LANG_CHOICES = [(_, _) for _ in ('Vietnamese', 'English', 'Other')]
CATEGORY_CHOICES = [(_, _) for _ in ('book', 'article', 'slide', 'test')]


class Document(models.Model):
	document_uuid = models.UUIDField(primary_key=True)
	title = models.CharField(max_length=255, null=False, blank=False)
	description = models.TextField(null=True, blank=True)
	release_year = models.SmallIntegerField(validators=[validate_year], null=True, blank=True)
	language = models.CharField(max_length=10, choices=LANG_CHOICES, null=False, blank=False)
	category = models.CharField(max_length=7, choices=CATEGORY_CHOICES, null=False, blank=False)
	path_to_file = models.FilePathField(null=False, auto_created=True, unique=True)
	upload_by = models.CharField(max_length=255, null=False, blank=False)
	last_update = models.DateTimeField(auto_now_add=True)

	class Meta:
		managed = True
		db_table = 'document'

	def __str__(self):
		return self.title
