from django.db import models

# Create your models here.

class Ensino(models.Model):
    nome = models.CharField(max_length=100, help_text="A etapa do ensino na educação em que a série está inserida, ex: Infantil, Fundamental, Médio, EJA")

class Serie(models.Model):
    ensino = models.ForeignKey(Ensino, on_delete=models.CASCADE, help_text="A etapa do ensino em que a série está inserida")
    nome = models.CharField(max_length=100, help_text="Nome da série, ex: Jardim 1")

class Organizacao(models.Model):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)

class Componente(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, help_text="A organização que a escola faz parte, ex: Prefeitura de São Judas")
    ensino = models.ForeignKey(Ensino, on_delete=models.CASCADE, help_text="A etapa do ensino em que este componente está inserido")
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)

class Instituicao(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, help_text="A organização que essa instituição de ensino faz parte, ex: Prefeitura de São Judas")
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=15)
