# Generated by Django 4.1.4 on 2023-01-30 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_usuario_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sopa_letras',
            old_name='id_usuario',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='trivia',
            old_name='id_usuario',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
