# Generated by Django 4.1.4 on 2023-01-31 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_delete_intensidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='id_comuna',
        ),
        migrations.RemoveField(
            model_name='profesional_salud',
            name='id_institucion',
        ),
        migrations.RemoveField(
            model_name='profesional_salud',
            name='user',
        ),
    ]