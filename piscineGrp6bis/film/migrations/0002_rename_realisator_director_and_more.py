# Generated by Django 4.2.7 on 2023-12-01 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Realisator',
            new_name='Director',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='realisator',
            new_name='director',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='realisator_bis',
            new_name='director_bis',
        ),
    ]