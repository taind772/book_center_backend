# import uuid
from .models import Document
import graphene
from graphene_django import DjangoObjectType


class DocumentServices():

  @staticmethod
  def get(*,
    uuid: graphene.UUID(required=True)
    )->graphene.Field:
    return Document.objects.get(document_uuid=uuid)

  @staticmethod
  def filter(*,
    title: graphene.String(),
    release_year: graphene.Int(),
    language: graphene.String(),
    category: graphene.String()
    )->graphene.List:
    """
    Filter document by title - release year - language - category
    """
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
      log.write(f'Query: title={title},language={language}, category={category}\nResultL {result}')
    return result.all()
  
  @staticmethod
  def create_document(*,
    title: graphene.String(),
    description: graphene.String(),
    release_year: graphene.Int(),
    language: graphene.String(),
    category: graphene.String()
  )->graphene.Boolean():
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