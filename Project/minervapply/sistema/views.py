from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *

# Create your views here.
def professor_logado(request,nome_professor):
    try:
        professor = Professor.objects.get(nome = nome_professor)
    except Professor.DoesNotExist:
        raise Http404('Professor não existente')
    context = {'lista_vagas_atual' : Vaga.objects.order_by('-prazo_de_aplicacao')}
    return render(request, 'sistema/professor_logado.html', context)

def formulario_vaga(request,nome_professor):
    return HttpResponse('Insira os dados da vaga:')
