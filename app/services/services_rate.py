from .models import Rate
from django.db.models import Avg
from user import services as UserServices
from document import services as DocumentServices


def rate_get(info) -> Rate:
    user = UserServices.user_get(info=info)
    return Rate.objects.filter(user_uuid=user.user_uuid)


def rate_get_all(document_uuid):
    return Rate.objects.filter(document_uuid=document_uuid)


def rate_add(info, document_uuid, rate_value, comment) -> Rate:
    user = UserServices.user_get(info=info)
    return Rate.objects.create(
        user_uuid=user.user_uuid,
        document_uuid=document_uuid,
        rate_value=rate_value,
        comment=comment)


def rate_delete(info, document_uuid):
    user = UserServices.user_get(info=info)
    rate = Rate.objects.get(user_uuid=user.user_uuid, document_uuid=document_uuid)
    rate.delete()
    return rate


def rate_get_user(rate):
    return UserServices.user_by_uuid(rate.user_uuid)


def rate_get_document(rate):
    return DocumentServices.document_by_uuid(rate.document_uuid)


def rate_get_average(document_uuid):
    rates = Rate.objects.filter(document_uuid=document_uuid)
    try:
        return rates.aggregate(Avg('rate_value'))
    except Rate.DoesNotExist:
        return 0