# Generated by Django 4.2.4 on 2023-11-04 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0004_alter_article_tittle_alter_article_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tittle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tittle',
            new_name='title',
        ),
    ]