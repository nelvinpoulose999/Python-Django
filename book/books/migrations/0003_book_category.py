# Generated by Django 3.2 on 2021-04-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_number_of_pages_book_book_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
