from django.db import models

# Create your models here.

# Ver https://www.estudokids.com.br/as-series-escolares-e-o-novo-ensino-fundamental-de-nove-anos/

class Ensino(models.Model):
    nome = models.CharField(max_length=100, help_text="A etapa do ensino na educação em que a série está inserida, ex: Infantil, Fundamental, Médio, EJA")
    
    def __str__(self):
        return self.nome

class Serie(models.Model):
    ensino = models.ForeignKey(Ensino, on_delete=models.CASCADE, help_text="A etapa do ensino em que a série está inserida")
    nome = models.CharField(max_length=100, help_text="Nome da série, ex: Jardim 1")
    def __str__(self):
        return self.nome + ' - ' + self.ensino.nome

    class Meta:
        verbose_name = "série"
        verbose_name_plural = "séries"

class Componente(models.Model):
    ensino = models.ForeignKey(Ensino, on_delete=models.CASCADE, help_text="A etapa do ensino em que este componente está inserido")
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

class Organizacao(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "organização"
        verbose_name_plural = "organizações"


class Instituicao(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, help_text="A organização que essa instituição de ensino faz parte, ex: Prefeitura de São Judas")
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "instituição"
        verbose_name_plural = "instituições"
