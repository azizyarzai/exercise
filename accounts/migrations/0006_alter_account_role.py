# Generated by Django 4.1 on 2022-10-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_account_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('developer', 'Developer'), ('designer', 'Designer')], default='developer', max_length=100),
        ),
    ]
