# Generated by Django 3.1.2 on 2020-10-27 16:32

from django.db import migrations, models
import document.validators


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_auto_20201027_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='release_year',
            field=models.SmallIntegerField(blank=True, null=True, validators=[document.validators.validate_year]),
        ),
    ]
