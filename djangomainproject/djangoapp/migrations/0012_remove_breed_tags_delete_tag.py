# Generated by Django 5.0 on 2023-12-17 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0011_delete_misc_breed_status_breed_where'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
