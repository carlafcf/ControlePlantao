# Generated by Django 3.0.3 on 2020-04-15 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20200415_1757'),
        ('plantao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantao',
            name='plantonista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantoes', to='usuario.User'),
        ),
    ]
