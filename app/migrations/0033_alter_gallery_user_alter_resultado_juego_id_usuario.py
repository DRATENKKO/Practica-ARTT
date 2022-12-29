# Generated by Django 4.1.4 on 2022-12-29 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_usuario_id_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.AlterField(
            model_name='resultado_juego',
            name='id_usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
    ]