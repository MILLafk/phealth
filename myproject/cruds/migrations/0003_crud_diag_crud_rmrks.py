# Generated by Django 4.2.13 on 2024-06-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0002_hosp'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='diag',
            field=models.CharField(default='default_value', max_length=200),
        ),
        migrations.AddField(
            model_name='crud',
            name='rmrks',
            field=models.CharField(default='default_value', max_length=200),
        ),
    ]
