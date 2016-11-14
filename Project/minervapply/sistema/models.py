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
    #lista_vagas_divulgadas = CommaSeparatedIntegerField(max_length=200)

"""    def __init__(self,nome,registro_ufrj,idade,departamento,email,telefone,url,chefe_departamento):
        self.nome=nome
        self.registro_ufrj=registro_ufrj
        self.idade=idade
        self.departamento=departamento
        self.email=email
        self.telefone=telefone
        self.url=url
        self.chefe_departamento=chefe_departamento
        #self.lista_vagas_divulgadas=lista_vagas_divulgadas

    def edit_personal_info(self, novo_nome):
        pass

    def lista_vagas_divulgadas(self):
        #buscar na database vagas com o mesmo id do professor_responsavel
        pass"""




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
    #professor_responsavel= models.ForeignKey('Professor')

    """def __init__(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        self.divulgar(disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel)

    def divulgar(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        self.disponilidade=disponilidade
        self.remuneracao=remuneracao
        self.local=local
        self.prazo_de_aplicacao=prazo_de_aplicacao
        self.tipo=tipo
        self.professor_responsavel=professor_responsavel
        self.add_to_database(disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel)

    def add_to_database(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        vaga = Vaga.object.get_or_create(disponilidade=disponibilidade,
                                        remuneracao=remuneracao,local=local,
                                        prazo_de_aplicacao=prazo_de_aplicacao,
                                        tipo=tipo,professor_responsavel=professor_responsavel)"""

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
