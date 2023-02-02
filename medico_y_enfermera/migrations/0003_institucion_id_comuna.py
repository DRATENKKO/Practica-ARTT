# Generated by Django 4.1.4 on 2023-02-02 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0009_provincia_id_region'),
        ('medico_y_enfermera', '0002_remove_institucion_id_comuna'),
    ]

    operations = [
        migrations.AddField(
            model_name='institucion',
            name='id_comuna',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tipologias.comuna'),
            preserve_default=False,
        ),
    ]