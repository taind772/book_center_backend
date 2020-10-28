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
    return UserServices.get_by_username(username=username)


class CreateUser(graphene.Mutation):
  class Arguments:
    username = graphene.String()
    email = graphene.String()
    password = graphene.String()
  
  user = graphene.Field(UserType)
  
  def mutate(self, info,
    username: graphene.String(),
    password: graphene.String(),
    email: graphene.String()
    )->graphene.Boolean:
    return CreateUser(
      user=UserServices.create_user(
        username=username, 
        email=email, 
        password=password
        ))


class Mutation(graphene.ObjectType):
  create_user = CreateUser.Field()