# Generated by Django 3.2.15 on 2022-12-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0007_auto_20221202_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='funcionamento',
            field=models.CharField(choices=[('funciona', 'Funciona'), ('estragado', 'Estragado')], default='func', max_length=9),
        ),
    ]