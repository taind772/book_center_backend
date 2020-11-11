import uuid
from .models import AbstractGroup, Author, Label, Publisher, models


class BaseServices:
    obj = AbstractGroup

    @classmethod
    def get_by_name(cls, name: str):
        return cls.obj.objects.get(name=name)

    @classmethod
    def get_by_id(cls, uid: uuid.UUID):
        return cls.obj.objects.get(id=uid)

    @classmethod
    def create(cls, name: str):
        name = cls.obj.normalize_name(name=name)
        return cls.obj.objects.create(name=name)

    @classmethod
    def get_all(cls, uuid_list=None):
        if uuid_list is None:
            return cls.obj.objects.all()
        return cls.obj.objects.filter(id__in=uuid_list)

    @classmethod
    def get_or_create(cls, name: str):
        name = cls.obj.normalize_name(name=name)
        res, _ = cls.obj.objects.get_or_create(name=name)
        return res


class AuthorServices(BaseServices):
    obj = Author


class LabelServices(BaseServices):
    obj = Label


class PublisherServices(BaseServices):
    obj = Publisher
