from django.db import models
from django.utils import timezone

class Vaga(models.Model):
    local = models.CharField(max_length=200)
    prazo_de_aplicacao = models.DateTimeField(default=timezone.now)

#este metodo eh soh pra testar!
def retorna_local(self):
    return self.local





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
