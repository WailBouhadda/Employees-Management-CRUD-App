# Generated by Django 4.2.5 on 2023-09-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
