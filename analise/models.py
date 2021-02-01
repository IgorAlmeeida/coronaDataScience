from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False, db_column='Nome')
    codigoUf = models.IntegerField(blank=False, null=False, db_column='CodigoUf')
    uf = models.CharField(max_length=2, blank=False, null=False, db_column='Uf')
    regiao = models.IntegerField(blank=False, null=False, db_column='Regiao')

class Cidade(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False, db_column='Nome')
    codigo = models.IntegerField(blank=False, null=False, db_column='Codigo')
    uf = models.CharField(max_length=2, blank=False, null=False, db_column='Uf') 