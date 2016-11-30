from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser


class Professor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #nome = models.CharField(max_length=100, default='nome')
    # registro_ufrj = models.CharField(max_length=8, default='000000-0')
    # idade = models.PositiveIntegerField(default=0)
    # departamento = models.CharField(max_length=200, default='nome_departamento')
    # email = models.EmailField(default='email@email.com')
    # telefone = models.CharField(max_length=20,default='0000-0000')
    # url = models.URLField(default='www.default.com')
    # chefe_departamento = models.BooleanField(default=False)
    # #lista_vagas_divulgadas = CommaSeparatedIntegerField(max_length=200)

    def __str__(self):
        return self.user.username






class Vaga(models.Model):
    IC='IC'
    ESTAGIO_EXT = 'EE'
    ESTAGIO_INT = 'EI'
    PROJETO = 'PROJ'
    BOLSA_CHOICES = (
        (IC, 'Iniciacao Cientifica'),
        (ESTAGIO_EXT, 'Estagio externo'),
        (ESTAGIO_INT, 'Estagio interno'),
        (PROJETO,'Projeto')
    )
    titulo = models.CharField(max_length=200, default='Titulo Vaga')
    disponibilidade = models.BooleanField(default=True)
    remuneracao = models.FloatField(default=0)
    local = models.CharField(max_length=200,default='local')
    data_publicacao = models.DateTimeField(default=timezone.now)
    prazo_de_aplicacao = models.DateField(default=timezone.now)
    tipo = models.CharField(max_length=4, choices = BOLSA_CHOICES, default=ESTAGIO_EXT)
    professor_responsavel= models.ForeignKey('Professor', null=True, blank=True)


    def __str__(self):
        return self.titulo

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Vaga._meta.fields]


    def add_to_database(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        vaga = Vaga.object.get_or_create(disponilidade=disponibilidade,
                                        remuneracao=remuneracao,local=local,
                                        prazo_de_aplicacao=prazo_de_aplicacao,
                                        tipo=tipo,professor_responsavel=professor_responsavel)

    def desativar_apos_selecao(self):
        self.disponibilidade=False
        self.save()

    def reativar(self):
        self.disponibilidade=True
        self.save()








"""class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title"""
