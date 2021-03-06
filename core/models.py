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

class MatrizCurricular(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, help_text="A organização que essa instituição de ensino faz parte, ex: Prefeitura de São Judas")
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=1024)
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "matriz curricular"
        verbose_name_plural = "matrizes curriculares"

class ComponenteMatriz(models.Model):
    '''
    Esta classe representa a carga horária de um componente na MatrizCurricular
    '''
    matriz = models.ForeignKey(MatrizCurricular, on_delete=models.CASCADE)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, help_text="Componente que irá compor a matriz curricular")
    carga_horaria = models.IntegerField("Carga horária", help_text="Carga horária semanal do componente nas séries.")
    series = models.ManyToManyField(Serie, help_text="As série que esse componente contém a carga horária especificada.")
    class Meta:
        verbose_name = "componente matriz"
        verbose_name_plural = "componentes matrizes"

'''
class PeriodoLetivo(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, help_text="A organização que essa instituição de ensino faz parte, ex: Prefeitura de São Judas")
    ano = models.IntegerField("Ano", help_text="Ano do período letivo")
    class Meta:
        verbose_name = "período letivo"
        verbose_name_plural = "períodos letivos"
'''