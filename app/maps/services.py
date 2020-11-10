import uuid

from document import services as DocumentServices
from groups.services import AuthorServices, PublisherServices, LabelServices
from .models import DocumentLabel, DocumentAuthor, DocumentPublisher


class DocumentLabelMap:
    @staticmethod
    def dl_create(label_uuid: uuid.UUID, document_uuid: uuid.UUID):
        return DocumentLabel.label_document_create(document_uuid=document_uuid, label_uuid=label_uuid)

    @staticmethod
    def dl_get_labels(document_uuid: uuid.UUID):
        label_uuid_list = DocumentLabel.objects.filter(document_uuid=document_uuid).values_list('group_uuid', flat=True)
        return LabelServices.get_all(label_uuid_list)

    @staticmethod
    def dl_get_documents(label_uuid: uuid.UUID):
        document_uuid_list = DocumentLabel.objects.filter(group_uuid=label_uuid).values_list('document_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)


class DocumentAuthorMap:
    @staticmethod
    def da_create(document_uuid: uuid.UUID, author_uuid: uuid.UUID):
        return DocumentAuthor.document_author_create(document_uuid=document_uuid, author_uuid=author_uuid)

    @staticmethod
    def da_get_documents(author_uuid: uuid.UUID):
        document_uuid_list = DocumentAuthor.objects.filter(group_uuid=author_uuid).values_list('document_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)

    @staticmethod
    def da_get_authors(document_uuid: uuid.UUID):
        author_uuid_list = DocumentAuthor.objects.filter(document_uuid=document_uuid).values_list('group_uuid', flat=True)
        return AuthorServices.get_all(uuid_list=author_uuid_list)


class DocumentPublisherMap:
    @staticmethod
    def dp_create(document_uuid: uuid.UUID, publisher_uuid: uuid.UUID):
        return DocumentPublisher.document_publisher_create(document_uuid=document_uuid, publisher_uuid=publisher_uuid)

    @staticmethod
    def dp_get_documents(publisher_uuid: uuid.UUID):
        document_uuid_list = DocumentPublisher.objects.filter(group_uuid=publisher_uuid)\
            .values_list('first_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)

    @staticmethod
    def dp_get_publishers(document_uuid: uuid.UUID):
        publisher_uuid_list = DocumentPublisher.objects.filter(document_uuid=document_uuid).\
            values_list('group_uuid', flat=True)
        return PublisherServices.get_all(uuid_list=publisher_uuid_list)
