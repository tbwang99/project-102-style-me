# Generated by Django 3.0.2 on 2020-02-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200223_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='major',
            field=models.CharField(default='', max_length=100),
        ),
    ]