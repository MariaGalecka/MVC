# Generated by Django 5.1.7 on 2025-06-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='Brak', max_length=100),
        ),
    ]
