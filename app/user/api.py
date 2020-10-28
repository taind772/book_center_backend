import graphene
from .services import UserServices


class UserType(graphene.ObjectType):
  user_uuid = graphene.UUID()
  username = graphene.String()
  email = graphene.String()
  last_update = graphene.DateTime()


class Query(graphene.ObjectType):
  #
  user_by_uuid = graphene.Field(UserType, uuid=graphene.UUID())
  
  def resolve_user_by_uuid(root, info, 
    uuid: graphene.UUID()
    )->graphene.Field:
    try:
      return UserServices.get(uuid=uuid)
    except:
      return None
  #
  user_by_username = graphene.Field(UserType, username=graphene.String())

  def resolve_user_by_username(root, info,
    username: graphene.String()
    )->graphene.Field:
    try:
      return UserServices.get(username=username)
    except:
      return None