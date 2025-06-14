# Generated by Django 5.1.7 on 2025-06-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100, verbose_name='Reżyser'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='Brak', max_length=100, verbose_name='Gatunek'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(verbose_name='Ocena'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Tytuł'),
        ),
    ]
