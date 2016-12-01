from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from .urls import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db import transaction
from .forms import *
from django.contrib import messages

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
        return Vaga.objects.filter(professor_responsavel=self.request.user.profile)



# class VagaView(DetailView):
#     model = Vaga
#     template_name = 'sistema/vaga_detail.html'

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse('tela-inicial'))
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@transaction.atomic
def create_user_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse('tela-inicial'))
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def is_professor(user):
    return user.profile.is_professor

class Criar_Vaga(CreateView):
    model = Vaga
    template_name_suffix = '_create'
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    context_object_name = "lista_vagas_professor"
    success_url = reverse_lazy('professor-logado')

    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    def dispatch(self, *args, **kwargs):
        return super(Criar_Vaga, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.professor_responsavel = self.request.user.profile
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
