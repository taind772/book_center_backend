import uuid
from .models import Document


class DocumentServices():

  @staticmethod
  def get(*,
    uuid: uuid.UUID
    )->Document:
    return Document.objects.get(document_uuid=uuid)

  @staticmethod
  def filter(*,
    title: str,
    release_year: int,
    language: str,
    category: str
    )->Document.objects:
    result = Document.objects
    if title is not None:
      result = result.filter(title=title)
    if release_year is not None:
      result = result.filter(release_year=release_year)
    if language is not None:
      result = result.filter(language=language)
    if category is not None:
      result = result.filter(category=category)
    with open('log/document-filter.log', 'a') as log:
      log.write(f'Query: title={title},language={language}, category={category}\nResult: {result}\n')
    return result.all()
  
  @staticmethod
  def create_document(*,
    title: str,
    description: str,
    release_year: int,
    language: str,
    category: str
  )->bool:
    try:
      document = Document.objects.create(
        title=title,
        description=description,
        release_year=release_year,
        category=category,
        language=language
      )
      return True
    except:
      return False