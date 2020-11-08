import uuid
import mimetypes
import os

import user.services as UserServices
import document.services as DocumentServices
from groups.services import AuthorServices, LabelServices, PublisherServices

from .models import Upload
from maps.services import DocumentAuthorMap, DocumentPublisherMap, LabelDocumentMap
from .drive_services import DriveServices

def write_to_drive(file, name):
    with open(f'tmp/{name}', 'wb') as f:
        for line in file:
            f.write(line)
    with open(f'tmp/{name}', 'rb') as f:
        res = DriveServices.upload_to_drive(file=f, name=name)
    os.remove(f'tmp/{name}')
    return res


def upload(info, title: str, description: str, release_year: int, language: str, category: str,
           authors_name: str, publishers: str, labels: str, file) -> Upload:
    user = UserServices.user_get(info=info)
    uid = uuid.uuid4()
    path_to_file = write_to_drive(file, uid.__str__())
    document = DocumentServices.document_create(
        uid=uid,
        title=title,
        description=description,
        release_year=release_year,
        language=language,
        category=category,
        uploader=user.username,
        path_to_file=path_to_file)
    if publishers is not None:
        for p_name in set((_.strip() for _ in publishers.split(','))):
            p = PublisherServices.get_or_create(name=p_name)
            DocumentPublisherMap.dp_create(document_uuid=document.document_uuid, publisher_uuid=p.id)
    if authors_name is not None:
        for a_name in set((_.strip() for _ in authors_name.split(','))):
            a = AuthorServices.get_or_create(name=a_name)
            DocumentAuthorMap.da_create(document_uuid=document.document_uuid, author_uuid=a.id)
    if labels is not None:
        for lb_name in set((_.strip() for _ in labels.split(','))):
            lb = LabelServices.get_or_create(name=lb_name)
            LabelDocumentMap.ld_create(document_uuid=document.document_uuid, label_uuid=lb.id)
    return Upload.objects.create(user_uuid=user.user_uuid, document_uuid=document.document_uuid)


# def remove(*, info, document_uuid: str)->bool:
#   user = UserServices.who_am_i(info=info)
#   owner = Upload.objects.get()


def upload_get_uploader(document_uuid: uuid.uuid4):
    user_uuid = Upload.objects.get(document_uuid=document_uuid).user_uuid
    return UserServices.user_by_uuid(user_uuid=user_uuid)


def upload_by_me(info):
    user = UserServices.user_get(info=info)
    document_uuid_list = Upload.objects.filter(user_uuid=user.user_uuid).values_list('document_uuid', flat=True)
    return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)
