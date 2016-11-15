from django.db import models
from django.utils import timezone
from datetime import date

class Professor(models.Model):
    nome = models.CharField(max_length=100, default='nome')
    registro_ufrj = models.CharField(max_length=8, default='000000-0')
    idade = models.PositiveIntegerField(default=0)
    departamento = models.CharField(max_length=200, default='nome_departamento')
    email = models.EmailField(default='email@email.com')
    telefone = models.CharField(max_length=20,default='0000-0000')
    url = models.URLField(default='www.default.com')
    chefe_departamento = models.BooleanField(default=False)
    #lista_vagas_divulgadas = CommaSeparatedIntegerField(max_length=200)

    def __str__(self):
        return self.nome



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
    titulo = models.CharField(max_length=200, default='Titulo Vaga')
    disponibilidade = models.BooleanField(default=True)
    remuneracao = models.FloatField(default=0)
    local = models.CharField(max_length=200,default='local')
    data_publicacao = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now())
    prazo_de_aplicacao = models.DateField(auto_now=False, auto_now_add=False, default=date.today())
    tipo = models.CharField(max_length=4, choices = BOLSA_CHOICES, default=ESTAGIO_EXT)
    professor_responsavel= models.ForeignKey('Professor', on_delete=models.CASCADE, default=0)

    """def __init__(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        self.divulgar(disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel)

    def divulgar(self,disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel):
        self.disponilidade=disponilidade
        self.remuneracao=remuneracao
        self.local=local
        self.prazo_de_aplicacao=prazo_de_aplicacao
        self.tipo=tipo
        self.professor_responsavel=professor_responsavel
        self.add_to_database(disponilidade,remuneracao,local,prazo_de_aplicacao,tipo,professor_responsavel)"""
    """def get_fields(self):
        return []"""


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
