# Generated by Django 4.1.12 on 2023-11-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_viaje__id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viaje',
            name='capacidadPasajeros',
        ),
        migrations.AlterField(
            model_name='viaje',
            name='_id',
            field=models.CharField(default='6558eba33951c6d132187b81', editable=False, max_length=24, primary_key=True, serialize=False),
        ),
    ]
