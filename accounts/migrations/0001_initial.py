# Generated by Django 3.0.2 on 2020-03-02 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(choices=[('Subject', 'SUBJECT'), ('APMA', 'Math'), ('CS', 'Computer Science'), ('COMM', 'Business'), ('BIOL', 'Biology'), ('CHEM', 'Chemistry')], default='Subject', max_length=17)),
                ('courseNumber', models.CharField(default='', max_length=50)),
                ('time', models.CharField(choices=[('5', '5 minutes'), ('15', '15 minutes'), ('30', '35 minutes'), ('60', '1 hour'), ('75', '1 hour 15 minutes'), ('90', '1.5 hour'), ('120', '2 hours')], default='5', max_length=17)),
                ('description', models.TextField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, max_length=100)),
                ('major', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]