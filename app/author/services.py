import uuid
from .models import Author

class AuthorServices():

  @staticmethod
  def filter(*, name: str)->Author:
    return Author.objects.get(name=name)

  @staticmethod
  def get(*, uuid: uuid.UUID)->Author:
    return Author.objects.get(author_uuid=uuid)

  @staticmethod
  def create(*, name: str, description: str)->bool:
    try:
      Author.objects.create(name=name, description=description)
      return True
    except:
      return False