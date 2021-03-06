# Generated by Django 3.1.5 on 2021-01-31 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='name',
        ),
        migrations.RemoveField(
            model_name='estado',
            name='sigla',
        ),
        migrations.AddField(
            model_name='estado',
            name='codigoUf',
            field=models.IntegerField(db_column='CodigoUf', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='nome',
            field=models.CharField(db_column='Nome', default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='regiao',
            field=models.IntegerField(db_column='Regiao', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estado',
            name='uf',
            field=models.CharField(db_column='Uf', default=1, max_length=2),
            preserve_default=False,
        ),
    ]
