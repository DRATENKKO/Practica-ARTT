# Generated by Django 4.1.4 on 2023-01-19 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_trivia_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sopa_letras',
            fields=[
                ('id_sopa', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
