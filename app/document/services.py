import uuid
from .models import Document


def document_create(uid: uuid.UUID, title: str, description: str, release_year: int, language: str,
                    category: str, uploader: str, path_to_file: str):
	return Document.objects.create(
		document_uuid=uid,
		title=title,
		description=description,
		release_year=release_year,
		language=language,
		category=category,
		upload_by=uploader,
		path_to_file=path_to_file)


def document_by_uuid(document_uuid: uuid.UUID) -> Document:
	return Document.objects.get(document_uuid=document_uuid)


def document_get_all(document_uuid_list=None):
	if document_uuid_list is None:
		return Document.objects.all()
	return Document.objects.filter(document_uuid__in=document_uuid_list)


def document_filter(title: str, release_year: int, language: str, category: str):
	result = Document.objects
	if title is not None:
		result = result.filter(title=title)
	if release_year is not None:
		result = result.filter(release_year=release_year)
	if language is not None:
		result = result.filter(language=language)
	if category is not None:
		result = result.filter(category=category)
	return result.all()
