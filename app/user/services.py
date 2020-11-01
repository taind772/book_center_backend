import uuid
from .models import User


def user_by_uuid(user_uuid: uuid.UUID) -> User:
    return User.objects.get(user_uuid=user_uuid)


def user_by_username(username: str) -> User:
    return User.objects.get(username=username)


def user_create(username: str, email: str, password: str) -> bool:
    user = User.objects.user_create(
            username=username,
            email=email,
            password=password)
    return user is not None


def user_get(info):
    user = info.context.user
    if user.is_anonymous:
        raise Exception('Not logged in!')
    return user
