import uuid
from .models import User


class UserServices():
  # 
  @staticmethod
  def get_by_uuid(*,
    uuid: uuid.UUID
    )->User:
    return User.objects.get(user_id=uuid)
  # 
  @staticmethod
  def get_by_username(*,
    username: str
    )->User:
    return User.objects.get(username=username)
  # 
  @staticmethod
  def create_user(*,
    username: str,
    email: str,
    password: str
    )->User:
    return User.objects.create(username=username, email=email, hash_pass=hash(password))
  # 