# Generated by Django 4.1.4 on 2023-01-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_sopa_letras'),
    ]

    operations = [
        migrations.AddField(
            model_name='sopa_letras',
            name='direction',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sopa_letras',
            name='start',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sopa_letras',
            name='word',
            field=models.CharField(max_length=50),
        ),
    ]
