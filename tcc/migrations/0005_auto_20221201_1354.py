# Generated by Django 3.2.15 on 2022-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcc', '0004_projetor_funcionamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.RenameField(
            model_name='projetor',
            old_name='description',
            new_name='descrição',
        ),
        migrations.RenameField(
            model_name='projetor',
            old_name='title',
            new_name='nome',
        ),
    ]
