# Generated by Django 3.2.13 on 2022-12-05 02:27

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
