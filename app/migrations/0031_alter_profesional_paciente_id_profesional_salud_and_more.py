# Generated by Django 4.1.4 on 2023-01-31 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_remove_institucion_id_comuna_and_more'),
        ('medico_y_enfermera', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional_paciente',
            name='id_profesional_salud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico_y_enfermera.profesional_salud'),
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.DeleteModel(
            name='Profesional_salud',
        ),
    ]
