from django.db import models
from django.utils import timezone

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    registro_ufrj = models.CharField(max_length=8)
    idade = models.PositiveIntegerField()
    departamento = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    url = models.URLField()
    chefe_departamento = models.BooleanField(default=False)

    def edit_personal_info(self, novo_nome):
        self.nome=novo_nome


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

    disponibilidade = models.BooleanField(default=True)
    remuneracao = models.FloatField(default=0)
    local = models.CharField(max_length=200)
    prazo_de_aplicacao = models.DateField(auto_now=False, auto_now_add=False)
    tipo = models.CharField(max_length=4, choices = BOLSA_CHOICES, default=ESTAGIO_EXT)

#este metodo eh soh pra testar!
    def retorna_local(self):
        return self.local

    def desativar_apos_selecao(self):
        self.disponibilidade=False

    def reativar(self):
        self.disponibilidade=True









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
