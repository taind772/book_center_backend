import uuid
from django.db import models


class AbstractPair(models.Model):
    first_uuid = models.UUIDField(null=False, blank=False)
    second_uuid = models.UUIDField(null=False, blank=False)

    class Meta:
        abstract = True


class DocumentAuthor(AbstractPair):
    class Meta:
        db_table = 'document_author'
        constraints = [
            models.UniqueConstraint(fields=['first_uuid', 'second_uuid'], name='authors_of_documents')
        ]

    def document_uuid(self):
        return self.first_uuid

    def author_uuid(self):
        return self.second_uuid

    @classmethod
    def document_author_create(cls, document_uuid: uuid.UUID, author_uuid: uuid.UUID):
        return cls.objects.get_or_create(first_uuid=document_uuid, second_uuid=author_uuid)


class DocumentPublisher(AbstractPair):
    class Meta:
        db_table = 'document_publisher'
        constraints = [
            models.UniqueConstraint(fields=['first_uuid', 'second_uuid'], name='documents_of_publisher')
        ]

    def document_uuid(self):
        return self.first_uuid

    def publisher_uuid(self):
        return self.second_uuid

    @classmethod
    def document_publisher_create(cls, document_uuid: uuid.UUID, publisher_uuid: uuid.UUID):
        return cls.objects.get_or_create(first_uuid=document_uuid, second_uuid=publisher_uuid)


class LabelDocument(AbstractPair):
    class Meta:
        db_table = 'document_label'
        constraints = [
            models.UniqueConstraint(fields=['first_uuid', 'second_uuid'], name='label_of_document')
        ]

    def label_uuid(self):
        return self.first_uuid

    def document_uuid(self):
        return self.second_uuid

    @classmethod
    def label_document_create(cls, document_uuid: uuid.UUID, label_uuid: uuid.UUID):
        return cls.objects.get_or_create(first_uuid=label_uuid, second_uuid=document_uuid)


# class LabelTopic(AbstractPair):
#     class Meta:
#         db_table = 'label_topic'
#         constraints = [
#             models.UniqueConstraint(fields=['first_uuid', 'second_uuid'], name='label_of_topic')
#         ]
#
#     def label_uuid(self):
#         return self.first_uuid
#
#     def topic_uuid(self):
#         return self.second_uuid
#
#     @classmethod
#     def label_topic_create(cls, label_uuid: uuid.UUID, topic_uuid: uuid.UUID):
#         return cls.objects.create(first_uuid=label_uuid, second_uuid=topic_uuid)
