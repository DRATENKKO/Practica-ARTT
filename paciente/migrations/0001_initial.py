# Generated by Django 4.1.4 on 2023-01-31 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id_diabetes', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_diabetes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hipertension',
            fields=[
                ('id_hipertension', models.AutoField(primary_key=True, serialize=False)),
                ('estado_hipertension', models.CharField(max_length=100)),
            ],
        ),
    ]
