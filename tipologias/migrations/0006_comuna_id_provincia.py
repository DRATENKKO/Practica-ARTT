# Generated by Django 4.1.4 on 2023-02-02 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipologias', '0005_provincia'),
    ]

    operations = [
        migrations.AddField(
            model_name='comuna',
            name='id_provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tipologias.provincia'),
            preserve_default=False,
        ),
    ]
