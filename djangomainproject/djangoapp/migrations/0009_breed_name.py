# Generated by Django 5.0 on 2023-12-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_rename_price_breed_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='breed',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
