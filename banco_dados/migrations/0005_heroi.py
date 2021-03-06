# Generated by Django 2.2.5 on 2019-09-27 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banco_dados', '0004_auto_20190927_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heroi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='nome')),
                ('idade', models.IntegerField()),
                ('fraqueza', models.CharField(max_length=255, verbose_name='fraqueza')),
                ('habilidade', models.ManyToManyField(related_name='heroi', to='banco_dados.Habilidade')),
                ('universo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_dados.Universo')),
            ],
        ),
    ]
