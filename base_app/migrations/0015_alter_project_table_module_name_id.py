# Generated by Django 4.0.3 on 2022-04-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0014_alter_project_module_assign_module'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_table',
            name='module_name_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
