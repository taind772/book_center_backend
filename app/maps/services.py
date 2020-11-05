import uuid

from document import services as DocumentServices
from groups.services import AuthorServices, PublisherServices, LabelServices
from .models import LabelDocument, DocumentAuthor, DocumentPublisher


# class LabelTopicMap:
#     @staticmethod
#     def lt_create(label_uuid: uuid.UUID, topic_uuid: uuid.UUID):
#         return LabelTopic.label_topic_create(label_uuid=label_uuid, topic_uuid=topic_uuid)
#
#     @staticmethod
#     def lt_get_labels(topic_uuid: uuid.UUID):
#         label_uuid_list = LabelTopic.objects.filter(second_uuid=topic_uuid).values_list('first_uuid', flat=True)
#         return LabelServices.get_all(uuid_list=label_uuid_list)


class LabelDocumentMap:
    @staticmethod
    def ld_create(label_uuid: uuid.UUID, document_uuid: uuid.UUID):
        return LabelDocument.label_document_create(document_uuid=document_uuid, label_uuid=label_uuid)

    @staticmethod
    def ld_get_labels(document_uuid: uuid.UUID):
        label_uuid_list = LabelDocument.objects.filter(second_uuid=document_uuid).values_list('first_uuid', flat=True)
        return LabelServices.get_all(label_uuid_list)

    @staticmethod
    def ld_get_documents(label_uuid: uuid.UUID):
        document_uuid_list = LabelDocument.objects.filter(first_uuid=label_uuid).values_list('second_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)


class DocumentAuthorMap:
    @staticmethod
    def da_create(document_uuid: uuid.UUID, author_uuid: uuid.UUID):
        return DocumentAuthor.document_author_create(document_uuid=document_uuid, author_uuid=author_uuid)

    @staticmethod
    def da_get_documents(author_uuid: uuid.UUID):
        document_uuid_list = DocumentAuthor.objects.filter(second_uuid=author_uuid).values_list('first_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)

    @staticmethod
    def da_get_authors(document_uuid: uuid.UUID):
        author_uuid_list = DocumentAuthor.objects.filter(first_uuid=document_uuid).values_list('second_uuid', flat=True)
        return AuthorServices.get_all(uuid_list=author_uuid_list)


class DocumentPublisherMap:
    @staticmethod
    def dp_create(document_uuid: uuid.UUID, publisher_uuid: uuid.UUID):
        return DocumentPublisher.document_publisher_create(document_uuid=document_uuid, publisher_uuid=publisher_uuid)

    @staticmethod
    def dp_get_documents(publisher_uuid: uuid.UUID):
        document_uuid_list = DocumentPublisher.objects.filter(second_uuid=publisher_uuid)\
            .values_list('first_uuid', flat=True)
        return DocumentServices.document_get_all(document_uuid_list=document_uuid_list)

    @staticmethod
    def dp_get_publishers(document_uuid: uuid.UUID):
        publisher_uuid_list = DocumentPublisher.objects.filter(first_uuid=document_uuid).\
            values_list('second_uuid', flat=True)
        return PublisherServices.get_all(uuid_list=publisher_uuid_list)
