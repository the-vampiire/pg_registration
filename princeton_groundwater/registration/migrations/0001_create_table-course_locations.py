# Generated by Django 2.0.2 on 2018-03-17 18:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=2000, null=True)),
                ('address', models.TextField(null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(message='Enter the phone number using an international format up to 15 digits. e.g. +18135550060 for a US country code (1) and area code (813)', regex='^\\+?\\d{8,15}$')])),
            ],
            options={
                'db_table': 'course_locations',
            },
        ),
    ]
