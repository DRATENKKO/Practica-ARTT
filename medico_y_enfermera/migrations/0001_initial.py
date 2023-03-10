# Generated by Django 4.1.4 on 2023-02-02 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_enfermera_neurologo',
            fields=[
                ('id_app_enfermera_neurologo', models.AutoField(primary_key=True, serialize=False)),
                ('username_enfermera', models.CharField(max_length=100)),
                ('username_neurologo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='App_enfermera_paciente',
            fields=[
                ('id_app_enfermera_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('username_enfermera', models.CharField(max_length=100)),
                ('username_paciente', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermera',
            fields=[
                ('id_enfermera', models.AutoField(primary_key=True, serialize=False)),
                ('rut_enfermera', models.CharField(max_length=100)),
                ('nombre_enfermera', models.CharField(max_length=100)),
                ('apellido_enfermera', models.CharField(max_length=100)),
                ('direccion_enfermera', models.CharField(max_length=100)),
                ('correo_enfermera', models.CharField(max_length=100)),
                ('telefono_enfermera', models.CharField(max_length=100)),
                ('whatsapp_enfermera', models.CharField(max_length=100)),
                ('telegram_enfermera', models.CharField(max_length=100)),
                ('celular_enfermera', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id_institucion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_institucion', models.CharField(max_length=100)),
                ('descripcion_institucion', models.CharField(max_length=100)),
                ('id_comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Profesional_salud',
            fields=[
                ('id_profesional_salud', models.AutoField(primary_key=True, serialize=False)),
                ('rut_profesional_salud', models.CharField(max_length=100)),
                ('id_institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico_y_enfermera.institucion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional_paciente',
            fields=[
                ('id_profesional_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
                ('id_profesional_salud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medico_y_enfermera.profesional_salud')),
            ],
        ),
    ]
