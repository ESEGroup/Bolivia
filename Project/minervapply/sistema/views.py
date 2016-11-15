from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *

# Create your views here.
def professor_logado(request,nome_professor):
    try:
        professor = Professor.objects.get(nome = nome_professor)
        lista_vagas = Vaga.objects.filter(disponibilidade = True)
    except Professor.DoesNotExist:
        raise Http404('Professor não existente')
    context = {'professor' : professor, 'lista_vagas' : lista_vagas}
    return render(request, 'sistema/professor_logado.html', context)

def formulario_vaga(request,nome_professor):
    return render(request,'sistema/ofertarVaga_br.html',{})
