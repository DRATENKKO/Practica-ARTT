# Generated by Django 4.1.4 on 2023-02-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_juego',
            fields=[
                ('id_tipo_juego', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_juego', models.CharField(max_length=100)),
            ],
        ),
    ]
