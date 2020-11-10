import uuid
from user import  services as UserServices
from document import services as DocumentServices
from .models import Bookmark


def bookmark_get(info):
    user = UserServices.user_get(info=info)
    document_uuid_list = Bookmark.objects.filter(user_uuid=user.user_uuid).values_list('document_uuid', flat=True)
    return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)


def bookmark_add(info, document_uuid: uuid.uuid4) -> Bookmark:
    user = UserServices.user_get(info=info)
    return Bookmark.objects.create(
        user_uuid=user.user_uuid,
        document_uuid=document_uuid)


def bookmark_delete(info, document_uuid: uuid.uuid4):
    user = UserServices.user_get(info=info)
    bookmark = Bookmark.objects.get(user_uuid=user.user_uuid, document_uuid=document_uuid)
    bookmark.delete()
    return bookmark


def bookmark_check(info, document_uuid: uuid.uuid4):
    user = UserServices.user_get(info=info)
    try:
        bookmark = Bookmark.objects.get(user_uuid=user.user_uuid, document_uuid=document_uuid)
        return bookmark is not None
    except Bookmark.DoesNotExist:
        return False
