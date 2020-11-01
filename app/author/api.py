import graphene
from . import services as AuthorServices


class AuthorType(graphene.ObjectType):
    author_uuid = graphene.UUID()
    name = graphene.String()
    description = graphene.String()
    last_update = graphene.DateTime()


class Query(graphene.ObjectType):
    #
    author_by_name = graphene.Field(AuthorType, name=graphene.String(required=True))

    @staticmethod
    def resolve_author_by_name(self, info, name: graphene.String()):
        return AuthorServices.author_by_name(name=name)
