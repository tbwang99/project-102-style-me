# Generated by Django 3.0.3 on 2020-02-20 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('math', 'MATH'), ('computer science', 'COMPUTER SCIENCE'), ('business', 'BUSINESS'), ('biology', 'BIOLOGY'), ('chemistry', 'CHEMISTRY')], default='computer science', max_length=17)),
            ],
        ),
    ]
