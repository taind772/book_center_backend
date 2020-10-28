import graphene
import document.api as DocumentApi
import author.api as AuthorApi

class Query(
    DocumentApi.Query,
    AuthorApi.Query,
    graphene.ObjectType
  ):
  pass

schema = graphene.Schema(query=Query)