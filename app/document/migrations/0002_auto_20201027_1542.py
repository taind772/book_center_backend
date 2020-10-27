# Generated by Django 3.1.2 on 2020-10-27 15:42

from django.db import migrations, models
import document.validators


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='release_year',
            field=models.IntegerField(blank=True, null=True, validators=[document.validators.validate_year]),
        ),
    ]