# Generated by Django 4.0.3 on 2022-04-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_user_registration_trainee_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_status',
            name='git_commit',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='test_status',
            name='git_link',
            field=models.TextField(default='', null=True),
        ),
    ]