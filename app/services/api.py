import graphene
from document.api import DocumentType
from user.api import UserType

from . import bookmark_services as BookmarkServices
from . import upload_services as UploadServices
from . import rate_services as RateServices

from user import services as UserServices


class RateType(graphene.ObjectType):
    rate_value = graphene.Int()
    document_uuid = graphene.UUID()
    username = graphene.String()

    def resolve_username(self, info):
        return UserServices.user_by_uuid(user_uuid=self.user_uuid).username


class Query(graphene.ObjectType):
    # bookmark
    bookmark_get = graphene.List(DocumentType)

    @staticmethod
    def resolve_bookmark_get(self, info):
        return BookmarkServices.bookmark_get(info=info)

    bookmark_check = graphene.Boolean(document_uuid=graphene.UUID())

    @staticmethod
    def resolve_bookmark_check(self, info, document_uuid):
        return BookmarkServices.bookmark_check(info=info, document_uuid=document_uuid)

    # upload
    upload_get_mines = graphene.List(DocumentType)

    @staticmethod
    def resolve_upload_get_mines(self, info):
        return UploadServices.upload_by_me(info=info)

    upload_get_uploader = graphene.Field(UserType, document_uuid=graphene.UUID(required=True))

    @staticmethod
    def resolve_upload_get_uploader(self, info, document_uuid):
        return UploadServices.upload_get_uploader(document_uuid=document_uuid)

    # rate
    rate_get_mines = graphene.List(RateType)

    @staticmethod
    def resolve_rate_get_mines(self, info):
        return RateServices.rate_get(info=info)

    rate_get_all = graphene.List(RateType, document_uuid=graphene.UUID(required=True))

    @staticmethod
    def resolve_rate_get_all(self, info, document_uuid):
        return RateServices.rate_get_all(document_uuid=document_uuid)


class BookmarkAdd(graphene.Mutation):
    class Arguments:
        document_uuid = graphene.UUID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, document_uuid):
        bookmark = BookmarkServices.bookmark_add(info=info, document_uuid=document_uuid)
        ok = bookmark is not None
        return BookmarkAdd(ok=ok)


class BookmarkDelete(graphene.Mutation):
    class Arguments:
        document_uuid = graphene.UUID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, document_uuid):
        deleted = BookmarkServices.bookmark_delete(info=info, document_uuid=document_uuid)
        ok = deleted is not None
        return BookmarkDelete(ok=ok)


class UploadDocument(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        release_year = graphene.Int()
        language = graphene.String(required=True)
        category = graphene.String(required=True)
        authors_name = graphene.String()
        publisher = graphene.String()
        topics = graphene.String()
        labels = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info,
               title,
               category,
               language,
               description=None,
               release_year=None,
               authors_name=None,
               publisher=None,
               topics=None,
               labels=None):
        upload = UploadServices.upload(
            info=info,
            title=title,
            category=category,
            language=language,
            description=description,
            release_year=release_year,
            authors_name=authors_name,
            publisher=publisher,
            topics=topics,
            labels=labels)
        ok = upload is not None
        return UploadDocument(ok=ok)


class RateAdd(graphene.Mutation):
    class Arguments:
        document_uuid = graphene.UUID(required=True)
        rate_value = graphene.Int(required=True)
        comment = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, document_uuid, rate_value, comment=None):
        rate = RateServices.rate_add(
                info=info,
                document_uuid=document_uuid,
                rate_value=rate_value,
                comment=comment)
        ok = rate is not None
        return RateAdd(ok=ok)


class RateDelete(graphene.Mutation):
    class Arguments:
        document_uuid = graphene.UUID(required=True)

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, document_uuid):
        rate = RateServices.rate_delete(info=info, document_uuid=document_uuid)
        ok = rate is not None
        return  RateDelete(ok=ok)


class Mutation(graphene.ObjectType):
    bookmark_add = BookmarkAdd.Field()
    bookmark_delete = BookmarkDelete.Field()
    document_upload = UploadDocument.Field()
    rate_add = RateAdd.Field()
    rate_delete = RateDelete.Field()
