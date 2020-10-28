import graphene
import document.api as DocumentApi
import author.api as AuthorApi
import user.api as UserApi

class Query(
    DocumentApi.Query,
    AuthorApi.Query,
    UserApi.Query,
    graphene.ObjectType
  ):
  pass

class Muatation(
    UserApi.Mutation
  ):
  pass

schema = graphene.Schema(query=Query, mutation=Muatation)