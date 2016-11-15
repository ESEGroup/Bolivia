from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .urls import *
# Create your views here.

"""def escolha_professor(request):
    context = {'lista_professores' : Professor.objects.all()}
    return render(request, 'sistema/escolha_professor.html', context)"""


def professor_logado(request,nome_professor):
    try:
        professor = Professor.objects.get(nome = nome_professor)
        lista_vagas = Vaga.objects.filter(disponibilidade = True)
    except Professor.DoesNotExist:
        raise Http404('Professor não existente')
    context = {'professor' : professor, 'lista_vagas' : lista_vagas}
    return render(request, 'sistema/professor_logado.html', context)


class Criar_Vaga(CreateView):
    model = Vaga
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    context_object_name = "lista_vagas_professor"
    success_url = reverse_lazy('professor-logado', args = ['Ticiana'])
    def get_professor(self):
        return self.kwargs['nome_professor']



class Atualizar_Vaga(UpdateView):
    model = Vaga
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    success_url = reverse_lazy('professor-logado',args = ['Ticiana'])



class Apagar_Vaga(DeleteView):
    model = Vaga
    success_url = reverse_lazy('professor-logado',args = ['Ticiana'])
    def get_professor(self):
        return self.kwargs['nome_professor']
