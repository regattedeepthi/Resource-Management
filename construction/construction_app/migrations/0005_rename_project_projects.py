# Generated by Django 5.1.4 on 2024-12-05 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('construction_app', '0004_rename_labour_ids_project_labour_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Projects',
        ),
    ]
