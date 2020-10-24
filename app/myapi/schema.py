import graphene
from graphene_django import DjangoObjectType
from .models import Authors, Documents, Users, Majors, Subjects, Publishers


class AuthorsType(DjangoObjectType):
  class Meta:
    model = Authors
    fields = ("name", "description")


class Query(graphene.ObjectType):
  all_author = graphene.List(AuthorsType)
  def resolve_all_author(root, info):
    try:
      return Authors.objects.all()
    except Authors.DoesNotExist:
      return None


schema = graphene.Schema(query=Query)