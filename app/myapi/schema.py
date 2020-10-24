import graphene
from graphene_django import DjangoObjectType
from .models import Authors, Bookmarks, DocumentAuthor, Documents, MajorSubject, Majors, Publishers, Rates, SubjectDocument, SubjectResource, Subjects, Uploaded, Users


class AuthorsType(DjangoObjectType):
  class Meta:
    model = Authors
    fields = ("name", "description")


class BookmarksType(DjangoObjectType):
  class Meta:
    model = Bookmarks
    fields = ("user", "document")


class DocumentAuthorType(DjangoObjectType):
  class Meta:
    model = DocumentAuthor
    fields = ("document", "author")


class DocumentsType(DjangoObjectType):
  class Meta:
    model = Documents
    fields = ("title", "description", "publisher", "release_year", "isbn", "language", "path_to_file", "category")


class MajorSubjectType(DjangoObjectType):
  class Meta:
    model = MajorSubject
    fields = ("major", "subject")


class MajorsType(DjangoObjectType):
  class Meta:
    model = Majors
    fields = ("name", "description")


class PublishersType(DjangoObjectType):
  class Meta:
    model = Publishers
    fields = ("name",)


class RatesType(DjangoObjectType):
  class Meta:
    model = Rates
    fields = ("document", "rate_value")


class SubjectDocumentType(DjangoObjectType):
  class Meta:
    model = SubjectDocument
    fields = ("subject", "document")


class SubjectResourceType(DjangoObjectType):
  class Meta:
    model = SubjectResource
    fields = ("subject", "resource")


class SubjectsType(DjangoObjectType):
  class Meta:
    model = Subjects
    fields = ("name", "description")


class UploadedType(DjangoObjectType):
  class Meta:
    model = Uploaded
    fields = ("user", "document", "upload_time")


class UsersType(DjangoObjectType):
  class Meta:
    model = Users
    fields = ("uname", "email", "md5_pass")


class Query(graphene.ObjectType):
  #
  all_author = graphene.List(AuthorsType)
  def resolve_all_author(root, info):
    try:
      return Authors.objects.all()
    except Authors.DoesNotExist:
      return None
  #
  bookmarks_by_user = graphene.Field(BookmarksType, user=graphene.Int())
  def resolve_bookmarks_by_user(root, info, user):
    try:
      return Bookmarks.objects.get(user=user)
    except Bookmarks.DoesNotExist:
      return None

schema = graphene.Schema(query=Query)