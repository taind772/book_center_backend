import graphene
import graphql_jwt
import document.api as DocumentApi
import user.api as UserApi
import services.api as ServicesApi
import groups.api as GroupsApi
import maps.api as MapsApi


class Query(
    DocumentApi.Query,
    UserApi.Query,
    ServicesApi.Query,
    GroupsApi.Query,
    MapsApi.Query,
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
