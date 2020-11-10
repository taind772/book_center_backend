import graphene

from document.api import DocumentType
from .services import DocumentAuthorMap, DocumentPublisherMap, DocumentLabelMap
from groups.api import GenericType


class Query(graphene.ObjectType):
    # document - author
    author_get_documents = graphene.List(DocumentType, author_uuid=graphene.UUID())

    @staticmethod
    def resolve_author_get_documents(self, info, author_uuid):
        return DocumentAuthorMap.da_get_documents(author_uuid=author_uuid)

    document_get_authors = graphene.List(GenericType, document_uuid=graphene.UUID())

    @staticmethod
    def resolve_document_get_authors(self, info, document_uuid):
        return DocumentAuthorMap.da_get_authors(document_uuid=document_uuid)

    # document - publisher
    publisher_get_documents = graphene.List(DocumentType, publisher_uuid=graphene.UUID())

    @staticmethod
    def resolve_publisher_get_documents(self, info, publisher_uuid):
        return DocumentPublisherMap.dp_get_documents(publisher_uuid=publisher_uuid)

    document_get_publishers = graphene.List(GenericType, document_uuid=graphene.UUID())

    @staticmethod
    def resolve_document_get_publishers(self, info, document_uuid):
        return DocumentPublisherMap.dp_get_publishers(document_uuid=document_uuid)

    # label - document
    label_get_documents = graphene.List(DocumentType, label_uuid=graphene.UUID())

    @staticmethod
    def resolve_label_get_documents(self, info, label_uuid):
        return DocumentLabelMap.dl_get_documents(label_uuid=label_uuid)

    document_get_labels = graphene.List(GenericType, document_uuid=graphene.UUID())

    @staticmethod
    def resolve_document_get_labels(self, info, document_uuid):
        return DocumentLabelMap.dl_get_labels(document_uuid=document_uuid)
