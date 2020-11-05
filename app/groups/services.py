import uuid
from .models import AbstractGroup, Author, Label, Publisher


class BaseServices:
    obj = AbstractGroup

    @classmethod
    def get_by_name(cls, name: str):
        return cls.obj.objects.get(name=name)

    @staticmethod
    def get_by_id(cls, _id: uuid.UUID):
        return cls.obj.objects.get(id=_id)

    @classmethod
    def create(cls, name: str):
        name = cls.obj.normalize_name(name=name)
        return cls.obj.objects.create(name=name)

    @classmethod
    def get_all(cls, uuid_list=None):
        if uuid_list is None:
            return cls.obj.objects.all()
        return cls.obj.objects.filter(uuid__in=uuid_list)

    @classmethod
    def get_or_create(cls, name: str, description=None):
        name = cls.obj.normalize_name(name=name)
        res, _ = cls.obj.objects.get_or_create(name=name, description=description)
        return res


class AuthorServices(BaseServices):
    obj = Author


class LabelServices(BaseServices):
    obj = Label


class PublisherServices(BaseServices):
    obj = Publisher
