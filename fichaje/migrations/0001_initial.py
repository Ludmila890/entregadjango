# Generated by Django 5.0.2 on 2024-03-14 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horas_cargadas', models.CharField(max_length=30)),
                ('tareas_realizadas', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]