from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField(null=True, blank=True)
    telefone = models.CharField(max_length=20,default='0000-0000')

    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    #Atributos exclusivos de Professor
    registro_ufrj = models.CharField(max_length=9, default='000000000')
    departamento = models.CharField(max_length=200, default='nome_departamento')
    url = models.URLField(default='www.default.com')
    chefe_departamento = models.BooleanField(default=False)

    #Atributos exclusivos de aluno
    curso = models.CharField(max_length=200, default='curso')
    dre = models.CharField(max_length=9, default='000000000')



    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

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
    professor_responsavel = models.ForeignKey('Profile', null=True, blank=True)
    candidatos = models.ManyToManyField( Profile, related_name='+')

    # def get_data_publicacao(self):
    #     return self.data_publicacao

    def __str__(self):
        return self.titulo
