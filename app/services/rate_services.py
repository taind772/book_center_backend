from .models import Rate
from user import services as UserServices


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
