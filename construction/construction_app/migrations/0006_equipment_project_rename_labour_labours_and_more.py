# Generated by Django 5.1.4 on 2024-12-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction_app', '0005_rename_project_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('labour_ids', models.IntegerField()),
                ('material_id', models.IntegerField(max_length=50)),
                ('material_quantity', models.IntegerField(max_length=200)),
                ('equipment_id', models.IntegerField(max_length=200)),
                ('equipment_quantity', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.RenameModel(
            old_name='Labour',
            new_name='Labours',
        ),
        migrations.RenameModel(
            old_name='Material',
            new_name='Materials',
        ),
        migrations.DeleteModel(
            name='Equipments',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
        migrations.RenameField(
            model_name='labours',
            old_name='name',
            new_name='labour_name',
        ),
        migrations.RenameField(
            model_name='materials',
            old_name='name',
            new_name='material_name',
        ),
    ]
