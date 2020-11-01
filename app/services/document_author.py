import uuid
from .models import DocumentAuthor


def create(document_uuid: uuid.uuid4, author_uuid: uuid.uuid4):
    return DocumentAuthor.objects.create(
        document_uuid=document_uuid,
        author_uuid=author_uuid)


def remove(document_uuid: uuid.uuid4, author_uuid: uuid.uuid4):
    obj = DocumentAuthor.objects.get(document_uuid=document_uuid, author_uuid=author_uuid)
    obj.delete()


def remove_by_document(document_uuid: uuid.uuid4):
    objs = DocumentAuthor.objects.filter(document_uuid=document_uuid)
    if objs.exists():
        for obj in objs:
            obj.delete()


def get_authors_uuid(document_uuid: uuid.uuid4):
    objs = DocumentAuthor.objects.filter(document_uuid=document_uuid)
    if objs.exists():
        author_uuid_list = objs.values_list('author_uuid', flat=True)
        return author_uuid_list
    return None


def get_documents_uuid(author_uuid: uuid.uuid4):
    objs = DocumentAuthor.objects.filter(author_uuid=author_uuid)
    if objs.exists():
        document_uuid_list = objs.values_list('document_uuid', flat=True)
        return document_uuid_list
    return None
