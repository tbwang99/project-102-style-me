# Generated by Django 3.0.2 on 2020-02-23 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200223_1330'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='website',
            new_name='major',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='city',
            new_name='year',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]