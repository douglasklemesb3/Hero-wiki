# Generated by Django 2.2.5 on 2019-09-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco_dados', '0002_categoria_habilidade_heroi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroi',
            name='idade',
            field=models.IntegerField(),
        ),
    ]