# Generated by Django 4.1.4 on 2022-12-28 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_gallery_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memorice',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Galeria',
        ),
        migrations.DeleteModel(
            name='Memorice',
        ),
    ]