import uuid
from .models import Document, models


def document_create(uid: uuid.UUID, title: str, description: str, release_year: int, language: str,
                    category: str, uploader: str, path_to_file: str, cover_url: str):
    return Document.objects.create(
        document_uuid=uid,
        title=title,
        description=description,
        release_year=release_year,
        language=language,
        category=category,
        upload_by=uploader,
        path_to_file=path_to_file,
        cover_url=cover_url)


def document_by_uuid(document_uuid: uuid.UUID) -> Document:
    return Document.objects.get(document_uuid=document_uuid)


def document_get_all(document_uuid_list=None) -> models.QuerySet:
    if document_uuid_list is None:
        return Document.objects.all()
    return Document.objects.filter(document_uuid__in=document_uuid_list)


def document_by_title(title):
    return Document.objects.filter(title__icontains=title)


def document_by_year(year):
    return Document.objects.filter(release_year=year)


def document_by_language(language):
    return Document.objects.filter(language=language)


def document_filter(title, year, language, category):
    documents = Document.objects
    if title is not None:
        documents = documents.filter(title__icontains=title)
    if year is not None:
        documents = documents.filter(release_year=year)
    if language is not None:
        documents = documents.filter(language=language)
    if category is not None:
        documents = documents.filter(category=category)
    return documents