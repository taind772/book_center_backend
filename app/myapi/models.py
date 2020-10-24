# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Bookmarks(models.Model):
    bookmark_id = models.AutoField(primary_key=True)
    document = models.ForeignKey('Documents', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bookmarks'
        unique_together = (('document', 'user'),)


class DocumentAuthor(models.Model):
    document = models.ForeignKey('Documents', models.DO_NOTHING)
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'document_author'
        unique_together = (('document', 'author'),)


LANG_CHOICES = [(_, _) for _ in ('vietnamese', 'english', 'other')]
CATEGORY_CHOICES = [(_, _) for _ in ('book', 'article', 'slide', 'test')]


class Documents(models.Model):
    doc_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey('Publishers', models.DO_NOTHING, blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10, choices=LANG_CHOICES)
    path_to_file = models.CharField(max_length=255)
    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)

    class Meta:
        managed = False
        db_table = 'documents'


class MajorSubject(models.Model):
    major = models.ForeignKey('Majors', models.DO_NOTHING)
    subject = models.ForeignKey('Subjects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'major_subject'
        unique_together = (('major', 'subject'),)


class Majors(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'majors'


class Publishers(models.Model):
    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'publishers'


class Rates(models.Model):
    rate_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    document = models.ForeignKey(Documents, models.DO_NOTHING)
    rate_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rates'
        unique_together = (('user', 'document'),)


class SubjectDocument(models.Model):
    subject = models.ForeignKey('Subjects', models.DO_NOTHING)
    document = models.ForeignKey(Documents, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'subject_document'
        unique_together = (('subject', 'document'),)


class SubjectResource(models.Model):
    subject = models.ForeignKey('Subjects', models.DO_NOTHING)
    resource = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'subject_resource'
        unique_together = (('subject', 'resource'),)


class Subjects(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subjects'


class Uploaded(models.Model):
    uploaded_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    document = models.ForeignKey(Documents, models.DO_NOTHING)
    upload_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploaded'
        unique_together = (('user', 'document'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    uname = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    md5_pass = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'