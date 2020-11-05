import graphene

from .services import AuthorServices, LabelServices, PublisherServices


class GenericType(graphene.ObjectType):
    id = graphene.UUID()
    name = graphene.String()
    description = graphene.String()
    last_update = graphene.DateTime()


class Query(graphene.ObjectType):
    # author
    author_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_author_by_name(self, info, name):
        return AuthorServices.get_by_name(name=name)

    author_by_uuid = graphene.Field(GenericType, name=graphene.UUID(required=True))

    @staticmethod
    def resolve_author_by_uuid(self, info, uuid):
        return AuthorServices.get_by_id(_id=uuid)

    # label
    label_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_label_by_name(self, info, name):
        return LabelServices.get_by_name(name=name)

    label_by_uuid = graphene.Field(GenericType, name=graphene.UUID(required=True))

    @staticmethod
    def resolve_label_by_uuid(self, info, uuid):
        return LabelServices.get_by_id(_id=uuid)

    # # topic
    # topic_by_name = graphene.Field(GenericType, name=graphene.String(required=True))
    #
    # @staticmethod
    # def resolve_topic_by_name(self, info, name):
    #     return LabelServices.get_by_name(name=name)
    #
    # topic_by_uuid = graphene.Field(GenericType, name=graphene.UUID(required=True))
    #
    # @staticmethod
    # def resolve_topic_by_uuid(self, info, uuid):
    #     return TopicServices.get_by_id(_id=uuid)

    # publisher
    publisher_by_name = graphene.Field(GenericType, name=graphene.String(required=True))

    @staticmethod
    def resolve_publisher_by_name(self, info, name):
        return PublisherServices.get_by_name(name=name)

    publisher_by_uuid = graphene.Field(GenericType, publisher_uuid=graphene.UUID())

    @staticmethod
    def resolve_publisher_by_uuid(self, info, publisher_uuid):
        return PublisherServices.get_by_id(_id=publisher_uuid)
