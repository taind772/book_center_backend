import graphene
from graphene_file_upload.scalars import Upload as Input
from document.api import DocumentType
from user.api import UserType

from . import services_bookmark as BookmarkServices
from . import services_upload as UploadServices
from . import services_rate as RateServices
from . import services_search as SearchServices


class RateType(graphene.ObjectType):
    rate_value = graphene.Int()
    comment = graphene.String()
    user = graphene.Field(UserType)
    document = graphene.Field(DocumentType)

    def resolve_username(self, info):
        return RateServices.rate_get_user(self)

    def resolve_document(self, info):
        return RateServices.rate_get_document(self)


class SearchResponse(graphene.ObjectType):
    has_next = graphene.Boolean()
    documents = graphene.List(DocumentType)


class Search(graphene.ObjectType):
    search_by_document_title = graphene.Field(SearchResponse,title=graphene.String(required=True),
                                             first=graphene.Int(), limit=graphene.Int())

    @staticmethod
    def resolve_search_by_document_title(self, info, title, **kwargs):
        return SearchServices.search_document_by_title(title=title, **kwargs)

    filter_document_by_year = graphene.Field(SearchResponse, year=graphene.Int(required=True),
                                             first=graphene.Int(), limit=graphene.Int())

    @staticmethod
    def resolve_filter_document_by_year(self, info, year, **kwargs):
        return SearchServices.search_document_by_year(year=year, **kwargs)

    filter_document_by_language = graphene.Field(SearchResponse, language=graphene.String(required=True),
                                                 first=graphene.Int(), limit=graphene.Int())
    @staticmethod
    def resolve_filter_document_by_language(self, info, language, **kwargs):
        return SearchServices.search_document_by_language(language=language, **kwargs)

    document_filter = graphene.Field(SearchResponse, title=graphene.String(),
                                     year=graphene.Int(), language=graphene.String(),
                                     first=graphene.Int(), limit=graphene.Int())
    @staticmethod
    def resolve_document_filter(self, info, **kwargs):
        return SearchServices.document_filter(**kwargs)


class Query(Search, graphene.ObjectType):
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

    rate_get_average = graphene.Float(document_uuid=graphene.UUID())

    @staticmethod
    def resolve_rate_get_average(self, info, document_uuid):
        return RateServices.rate_get_average(document_uuid=document_uuid)


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
        publishers = graphene.String()
        labels = graphene.String()
        file = Input(required=True)
        cover_url = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(self, info, title, category, language, file,
               description=None, release_year=None,
               authors_name=None, publishers=None,
               labels=None, cover_url=None):
        upload = UploadServices.upload(
            info=info,
            title=title,
            category=category,
            language=language,
            description=description,
            release_year=release_year,
            authors_name=authors_name,
            publishers=publishers,
            labels=labels,
            file=file,
            cover_url=cover_url)
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
