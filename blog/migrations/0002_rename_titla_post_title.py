# Generated by Django 3.2.25 on 2024-06-01 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titla',
            new_name='title',
        ),
    ]
