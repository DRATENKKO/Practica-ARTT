# Generated by Django 4.1.4 on 2023-02-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_usuario',
            fields=[
                ('id_tipo_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo_usuario', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
