import uuid
from .models import Upload
import user.services as UserServices
import document.services as DocumentServices
import author.services as AuthorServices
from . import document_author as DocumentAuthorMap


def upload(info,
           title: str,
           description: str,
           release_year: int,
           language: str,
           category: str,
           authors_name: str
           ) -> bool:
    user = UserServices.user_get(info=info)
    document = DocumentServices.document_create(
        title=title,
        description=description,
        release_year=release_year,
        language=language,
        category=category,
        authors_name=authors_name,
        uploader=user.username)
    if authors_name is not None:
        for a_name in authors_name.split(','):
            author = AuthorServices.author_by_name(name=a_name)
            if author is None:
                author = AuthorServices.author_create(author_name=a_name)
            DocumentAuthorMap.create(
                document_uuid=document.document_uuid,
                author_uuid=author.author_uuid)
    Upload.objects.create(
        user_uuid=user.user_uuid,
        document_uuid=document.document_uuid)
    return True


# def remove(*, info, document_uuid: str)->bool:
#   user = UserServices.who_am_i(info=info)
#   owner = Upload.objects.get()


def get_uploader(document_uuid: uuid.uuid4):
    uploader_uuid = Upload.objects.get(document_uuid=document_uuid).user_uuid
    return UserServices.user_by_uuid(user_uuid=uploader_uuid)


def upload_by_me(info):
    user = UserServices.user_get(info=info)
    return Upload.objects.filter(user_uuid=user.user_uuid)
