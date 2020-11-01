import graphene
import graphql_jwt
import document.api as DocumentApi
import author.api as AuthorApi
import user.api as UserApi
import services.api as ServicesApi


class Query(
    DocumentApi.Query,
    AuthorApi.Query,
    UserApi.Query,
    ServicesApi.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    UserApi.Mutation,
    ServicesApi.Mutation
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
