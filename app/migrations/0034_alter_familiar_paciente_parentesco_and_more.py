# Generated by Django 4.1.4 on 2023-02-01 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_tipo_parentescoo'),
        ('app', '0033_delete_familiar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar_paciente',
            name='parentesco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.tipo_parentescoo'),
        ),
        migrations.DeleteModel(
            name='Tipo_parentesco',
        ),
    ]
