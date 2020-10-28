import uuid
from .models import User


class UserServices():

  @staticmethod
  def get_by_uuid(*,
    uuid: uuid.UUID
    )->User:
    return User.objects.get(user_id=uuid)
  
  @staticmethod
  def get_by_username(*,
    username: str
    )->User:
    return User.objects.get(username=username)