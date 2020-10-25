import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Authors, Bookmarks, DocumentAuthor, Documents, MajorSubject, Majors, Publishers, Rates, SubjectDocument, SubjectResource, Subjects, Uploaded, Users


class AuthorsType(DjangoObjectType):
  class Meta:
    model = Authors
    fields = ("name", "description")


class AddAuthor(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    description = graphene.String()

  author = graphene.Field(AuthorsType)

  def mutate(self, info, name, description=None):
    author = Authors(name=name, description=description)
    author.save()
    return AddAuthor(author=author)


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


class AddDocument(graphene.Mutation):
  class Arguments:
    title = graphene.String(required=True)
    description = graphene.String()
    publisher = graphene.String()
    release_year = graphene.Int()
    isbn = graphene.String()
    language = graphene.Int()
    category = graphene.String(required=True)
  
  document = graphene.Field(DocumentsType)

  def mutate(self, info, title, category, description=None, publisher=None, release_year=None, isbn=None, language=1):
    document = Documents(title=title, path_to_file="auto", category=category, description=description, publisher=publisher, release_year=release_year, isbn=isbn, language=language)
    document.save()
    return AddDocument(document=document)


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


class CreateUser(graphene.Mutation):
  class Arguments:
    uname = graphene.String()
  user = graphene.Field(UsersType)

  def mutate(self, info, uname):
    user = Users(uname=uname, email="any", md5_pass="")
    return CreateUser(user=user)


class Query(graphene.ObjectType):
  # About Author:
  authors = DjangoListField(AuthorsType)
  
  author_by_name = graphene.List(AuthorsType, name=graphene.String())
  def resolve_author_by_name(root, info, name):
    try:
      return Authors.objects.get(name=name)
    except Authors.DoesNotExist:
      return None
  # About 
  bookmarks_by_user = graphene.Field(BookmarksType, user=graphene.Int())
  def resolve_bookmarks_by_user(root, info, user):
    try:
      return Bookmarks.objects.get(user=user)
    except Bookmarks.DoesNotExist:
      return None


class Mutations(graphene.ObjectType):
  add_author = AddAuthor.Field()
  add_document = AddDocument.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)