import graphene
from . import services as DocumentServices


class DocumentType(graphene.ObjectType):
    document_uuid = graphene.UUID()
    title = graphene.String()
    description = graphene.String()
    release_year = graphene.Int()
    language = graphene.String()
    category = graphene.String()
    last_update = graphene.DateTime()
    authors_name = graphene.String()
    upload_by = graphene.String()


class Query(graphene.ObjectType):
    #
    document_by_uuid = graphene.Field(DocumentType, uuid=graphene.UUID(required=True))

    @staticmethod
    def resolve_document_by_uuid(self, info, uuid: graphene.UUID()):
        return DocumentServices.document_by_uuid(document_uuid=uuid)

    #
    document_filter = graphene.List(
        DocumentType,
        title=graphene.String(),
        release_year=graphene.Int(),
        language=graphene.String(),
        category=graphene.String())

    @staticmethod
    def resolve_document_filter(self, info, title=None, release_year=None, language=None, category=None):
        return DocumentServices.document_filter(
            title=title,
            release_year=release_year,
            language=language,
            category=category)

    # document_get_author = graphene.List(graphene.ObjectType, document_uuid=graphene.UUID())
    #
    # @staticmethod
    # def resolve_document_get_author(self, info, document_uuid: graphene.UUID()):
    #     author_uuid_list = DocumentAuthorMap.get_authors_uuid(document_uuid=document_uuid)
    #     return AuthorServices.author_get_all(author_uuid_list=author_uuid_list)
