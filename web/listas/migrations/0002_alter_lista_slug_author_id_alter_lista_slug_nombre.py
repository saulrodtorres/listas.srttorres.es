# Generated by Django 5.0.6 on 2024-05-21 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='slug_author_id',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='lista',
            name='slug_nombre',
            field=models.SlugField(blank=True),
        ),
    ]
