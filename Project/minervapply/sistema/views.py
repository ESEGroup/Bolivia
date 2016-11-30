from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .urls import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class TelaInicial(ListView):
    model = Vaga
    template_name = 'sistema/lista_vagas.html'

class ProfessorLogado(ListView):
    model = Vaga
    template_name = 'sistema/vaga_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfessorLogado, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Vaga.objects.filter(professor_responsavel=self.request.user.professor)



# class VagaView(DetailView):
#     model = Vaga
#     template_name = 'sistema/vaga_detail.html'



class Criar_Vaga(CreateView):
    model = Vaga
    template_name_suffix = '_create'
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    context_object_name = "lista_vagas_professor"
    success_url = reverse_lazy('professor-logado')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Criar_Vaga, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.professor_responsavel = self.request.user.professor
        return super(Criar_Vaga, self).form_valid(form)




class Atualizar_Vaga(UpdateView):
    model = Vaga
    template_name_suffix = '_edit'
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    success_url = reverse_lazy('professor-logado')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Atualizar_Vaga, self).dispatch(*args, **kwargs)



class Apagar_Vaga(DeleteView):
    model = Vaga
    success_url = reverse_lazy('professor-logado')
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Apagar_Vaga, self).dispatch(*args, **kwargs)
