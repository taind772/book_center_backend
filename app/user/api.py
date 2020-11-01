import graphene
from . import services as  UserServices


class UserType(graphene.ObjectType):
	username = graphene.String()
	join_date = graphene.DateTime()


class UserCreate(graphene.Mutation):
	class Arguments:
		username = graphene.String(required=True)
		email = graphene.String(required=True)
		password = graphene.String(required=True)

	ok = graphene.Boolean()

	@staticmethod
	def mutate(self, info, username, password, email):
		return UserCreate(
			ok=UserServices.user_create(
				username=username,
				email=email,
				password=password))


class Mutation(graphene.ObjectType):
	user_create = UserCreate.Field()


class Query(graphene.ObjectType):
	#
	user_by_username = graphene.Field(UserType, username=graphene.String(required=True))

	@staticmethod
	def resolve_user_by_username(self, info, username):
		return UserServices.user_by_username(username=username)

	#
	user_get = graphene.Field(UserType)

	@staticmethod
	def resolve_user_get(self, info):
		return UserServices.user_get(info=info)
