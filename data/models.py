from django.db import models

# Create your models here.
class MaioresDividendos(models.Model):
    codigo = models.CharField(max_length=50)
    dividendo_atual = models.DecimalField(max_digits=5, decimal_places=2)
    dividendo_medio = models.DecimalField(max_digits=5, decimal_places=2)
    p_l = models.DecimalField(max_digits=6, decimal_places=2)
    p_vp = models.DecimalField(max_digits=6, decimal_places=2)
    margem_liquida = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mercado = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    data = models.DateField()

    class Meta:
        verbose_name = 'Maior Dividendo'
        verbose_name_plural = 'Maiores Dividendos'
        ordering = ['-setor']

class MaioresDividendosMedio(models.Model):
    codigo = models.CharField(max_length=50)
    dividendo_atual = models.DecimalField(max_digits=5, decimal_places=2)
    dividendo_medio = models.DecimalField(max_digits=5, decimal_places=2)
    p_l = models.DecimalField(max_digits=6, decimal_places=2)
    p_vp = models.DecimalField(max_digits=6, decimal_places=2)
    margem_liquida = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mercado = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    data = models.DateField()

    class Meta:
        verbose_name = 'Maior Dividendo Médio'
        verbose_name_plural = 'Maiores Dividendos Medio'
        ordering = ['-setor']

class MaioresLucros(models.Model):
    codigo = models.CharField(max_length=50)
    lucro = models.DecimalField(max_digits=20, decimal_places=2)
    p_l = models.DecimalField(max_digits=6, decimal_places=2)
    p_vp = models.DecimalField(max_digits=6, decimal_places=2)
    margem_liquida = models.DecimalField(max_digits=6, decimal_places=2)
    valor_mercado = models.CharField(max_length=50)
    dividendo_medio = models.DecimalField(max_digits=5, decimal_places=2)
    setor = models.CharField(max_length=50)
    data = models.DateField()

    class Meta:
        verbose_name = 'Maior Lucro'
        verbose_name_plural = 'Maiores Lucros'
        ordering = ['-lucro']

