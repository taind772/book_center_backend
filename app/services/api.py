import graphene
from document.api import DocumentType

from . import bookmark_services as BookmarkServices
from . import upload_services as UploadServices


class Query(graphene.ObjectType):
    # bookmark
    bookmark_get = graphene.List(DocumentType)

    @staticmethod
    def resolve_bookmark_get(self, info):
        return BookmarkServices.bookmark_get(info=info)

    bookmark_create = graphene.Boolean(document_uuid=graphene.UUID())

    @staticmethod
    def resolve_bookmark_create(self, info, document_uuid):
        return BookmarkServices.bookmark_create(info=info, document_uuid=document_uuid)

    bookmark_check = graphene.Boolean(document_uuid=graphene.UUID())

    @staticmethod
    def resolve_bookmark_check(self, info, document_uuid: graphene.UUID()):
        return BookmarkServices.bookmark_check(info=info, document_uuid=document_uuid)

    bookmark_delete = graphene.Boolean(document_uuid=graphene.UUID())

    @staticmethod
    def resolve_bookmark_delete(self, info, document_uuid: graphene.UUID()):
        return BookmarkServices.bookmark_delete(info=info, document_uuid=document_uuid)

    # upload
    upload_get = graphene.List(DocumentType)

    @staticmethod
    def resolve_upload_get(self, info):
        return UploadServices.upload_by_me(info=info)


class UploadDocument(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        release_year = graphene.Int()
        language = graphene.String(required=True)
        category = graphene.String(required=True)
        authors_name = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info,
               title,
               category,
               language,
               description=None,
               release_year=None,
               authors_name=None):
        return UploadDocument(
            ok=UploadServices.upload(
                info=info,
                title=title,
                category=category,
                language=language,
                description=description,
                release_year=release_year,
                authors_name=authors_name
            ))


class Mutation(graphene.ObjectType):
    document_upload = UploadDocument.Field()
