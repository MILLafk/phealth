# Generated by Django 4.2.13 on 2024-06-28 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phealth_no', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('middleName', models.CharField(max_length=200)),
                ('published_date', models.DateField()),
            ],
        ),
    ]
