import uuid
from user import  services as UserServices
from .models import Bookmark


def bookmark_get(info):
    user = UserServices.user_get(info=info)
    return Bookmark.objects.filter(user_uuid=user.user_uuid)


def bookmark_create(info, document_uuid: uuid.uuid4) -> bool:
    user = UserServices.user_get(info=info)
    bookmark = Bookmark.objects.create(
        user_uuid=user.user_uuid,
        document_uuid=document_uuid)
    return bookmark is not None


def bookmark_delete(info, document_uuid: uuid.uuid4):
    user = UserServices.user_get(info=info)
    bookmark = Bookmark.objects.get(
        user_uuid=user.user_uuid,
        document_uuid=document_uuid)
    if bookmark is not None:
        bookmark.delete()


def bookmark_check(info, document_uuid: uuid.uuid4):
    user = UserServices.user_get(info=info)
    bookmark = Bookmark.objects.get(user_uuid=user.user_uuid, document_uuid=document_uuid)
    return bookmark is not None
