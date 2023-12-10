# Generated by Django 4.2.7 on 2023-12-07 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_url',
            field=models.ImageField(upload_to=''),
        ),
    ]
