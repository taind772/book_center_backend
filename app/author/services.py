import uuid
from .models import Author


def author_by_name(name: str):
    try:
        return Author.objects.get(name=name)
    except Author.DoesNotExist:
        return None


def author_get(author_uuid: uuid.UUID):
    return Author.objects.get(author_uuid=author_uuid)


def author_create(author_name: str):
    return Author.objects.create(name=author_name)


def author_get_all(author_uuid_list=None):
    if author_uuid_list is None:
        return Author.objects.all()
    return Author.objects.filter(author_uuid__in=author_uuid_list)
