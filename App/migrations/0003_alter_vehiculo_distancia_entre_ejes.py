# Generated by Django 4.2.6 on 2024-11-08 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_vehiculo_combustible_remove_vehiculo_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='distancia_entre_ejes',
            field=models.FloatField(default='1.5'),
        ),
    ]
