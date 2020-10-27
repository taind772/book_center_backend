# from .services import DocumentServices
import graphene
from .services import DocumentServices


class DocumentType(graphene.ObjectType):
  uuid = graphene.UUID()
  title = graphene.String()
  description = graphene.String()
  release_year = graphene.Int()
  language = graphene.String()
  category = graphene.String()
  last_update = graphene.DateTime()


class Query(graphene.ObjectType):

  document_by_uuid = graphene.Field(DocumentType, uuid=graphene.UUID())

  def resolve_document_by_uuid(root, info, 
    uuid: graphene.UUID()
    )->graphene.Field:
    try:
      return DocumentServices.get(uuid=uuid)
    except:
      None
  #
  document_filter = graphene.List(
    DocumentType,
    title=graphene.String(),
    release_year=graphene.Int(),
    language=graphene.String(),
    category=graphene.String()
    )

  def resolve_document_filter(root, info,
    title=None,
    release_year=None,
    language=None,
    category=None
    )->graphene.List:
    return DocumentServices.filter(
      title=title,
      release_year=release_year,
      language=language,
      category=category
    )



# class AddDocument(graphene.Mutation):
#   class Arguments:
#     title = graphene.String(required=True)
#     description = graphene.String()
#     release_year = graphene.Int()
#     language = graphene.Enum()
#     category = graphene.Enum()
  
#   # document = graphene.Field(DocumentsType)
#   ok = graphene.Boolean()

#   def mutate(self, info, title, category, language, description=None, release_year=None):
#     return AddDocument(
#       ok=DocumentServices.create_document(
#         title=title,
#         description=description,
#         release_year=release_year,
#         language=language,
#         category=category
#       )
#     )


# class Mutation(graphene.ObjectType):
#   add_document = AddDocument.Field()


schema = graphene.Schema(query=Query)