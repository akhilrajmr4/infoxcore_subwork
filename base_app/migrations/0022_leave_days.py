# Generated by Django 4.0.2 on 2022-05-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0021_acntspayslip_account_no_acntspayslip_bank_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='days',
            field=models.IntegerField(default=0),
        ),
    ]
