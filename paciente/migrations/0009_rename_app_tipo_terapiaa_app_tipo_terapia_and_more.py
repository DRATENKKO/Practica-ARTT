# Generated by Django 4.1.4 on 2023-01-31 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0008_intensidad'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='App_tipo_terapiaa',
            new_name='App_tipo_terapia',
        ),
        migrations.RenameModel(
            old_name='Terapiaa',
            new_name='Terapia',
        ),
    ]
