# Generated by Django 4.2.7 on 2023-12-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_alter_movie_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]
