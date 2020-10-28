import graphene
from .services import AuthorServices

class AuthorType(graphene.ObjectType):
  author_uuid = graphene.UUID()
  name = graphene.String()
  description = graphene.String()
  last_update = graphene.DateTime()


class Query(graphene.ObjectType):
  #
  author_by_name = graphene.Field(AuthorType, name=graphene.String())

  def resolve_author_by_name(root, info,
    name: graphene.String()
    )->graphene.Field:
    try:
      return AuthorServices.filter(name=name)
    except:
      return None
  #
  author_by_uuid = graphene.Field(AuthorType, uuid=graphene.UUID(required=True))

  def resolve_author_by_uuid(root, info,
    uuid: graphene.UUID()
    )->graphene.Field:
    try:
      return AuthorServices.get(uuid=uuid)
    except:
      return None