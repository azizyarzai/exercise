# Generated by Django 4.1 on 2022-10-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_is_active_account_is_stuff_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_stuff',
            new_name='is_staff',
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('developer', 'Developer'), ('designer', 'Designer')], max_length=100),
        ),
    ]