from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import MultipleObjectsReturned

from .forms import *
from .urls import *
from .models import Profile, Vaga

def is_aluno(self):
    return self.profile.is_aluno
def is_professor(self):
    return self.profile.is_professor
def is_chefe_departamento(self):
    return self.profile.chefe_departamento
def is_admin(self):
    return self.profile.is_admin

"""------------------------------ MOSTRAR VAGAS -----------------------------"""

class TelaInicial(ListView):
    model = Vaga
    template_name = 'sistema/vaga_list.html'
    def get_queryset(self):
        return sorted(Vaga.objects.filter(candidato_selecionado = None), key=lambda vaga: vaga.data_publicacao, reverse=True)

class ProfessorLogado(ListView):
    model = Vaga
    template_name = 'sistema/vaga_list_professor.html'
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    def dispatch(self, *args, **kwargs):
        return super(ProfessorLogado, self).dispatch(*args, **kwargs)
    def get_queryset(self):
        return sorted(Vaga.objects.filter(professor_responsavel=self.request.user.profile), key=lambda vaga: vaga.data_publicacao, reverse=True)

"""--------------- CREACAO, EDICAO E DELETADO DE VAGAS ---------------------"""

class Criar_Vaga(SuccessMessageMixin,CreateView):
    model = Vaga
    template_name_suffix = '_create'
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    context_object_name = "lista_vagas_professor"
    success_url = reverse_lazy('professor-logado')
    success_message = "Vaga criada com succeso"
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    def dispatch(self, *args, **kwargs):
        return super(Criar_Vaga, self).dispatch(*args, **kwargs)
    def form_valid(self, form):
        form.instance.professor_responsavel = self.request.user.profile
        return super(Criar_Vaga, self).form_valid(form)

class Atualizar_Vaga(SuccessMessageMixin,UpdateView):
    model = Vaga
    template_name_suffix = '_edit'
    fields = ['titulo','remuneracao','local','prazo_de_aplicacao','tipo']
    success_url = reverse_lazy('professor-logado')
    success_message = "Vaga atualizada com succeso"
    def test_autoria(self, request):
        return self.get_object().professor_responsavel.user == request.user
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    def dispatch(self, request, *args, **kwargs):
        if not self.test_autoria(request):
            return redirect_to_login(request.get_full_path())
        return super(Atualizar_Vaga, self).dispatch(
            request, *args, **kwargs)

class Apagar_Vaga(SuccessMessageMixin,DeleteView):
    model = Vaga
    success_url = reverse_lazy('professor-logado')
    success_message = "Vaga apagada com succeso"
    def test_autoria(self, request):
        return self.get_object().professor_responsavel.user == request.user
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    def dispatch(self, request, *args, **kwargs):
        if not self.test_autoria(request):
            return redirect_to_login(request.get_full_path())
        return super(Apagar_Vaga, self).dispatch(
            request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Apagar_Vaga, self).delete(request, *args, **kwargs)

"""----------- CANDIDATARSE VAGAS, MOSTRAR CANDIDATOS, SELECCIONAR ----------"""

@login_required
@user_passes_test(is_aluno)
def candidatarse(request,pk):
    try:
        vaga = Vaga.objects.get(pk = pk)
        vaga.candidatos.add(request.user.profile)
        vaga.save()
        messages.success(request,'Succesfully applied for vaga %s' % vaga)
        return redirect(reverse('tela-inicial'))
    except Vaga.DoesNotExist:
        raise Http404("Vaga não existe")
    except MultipleObjectsReturned:
        raise Http404("Devolveu mais de um objeto")

@login_required
@user_passes_test(is_aluno)
def aluno_candidatadas(request):
    aluno = request.user.profile
    lista_vagas_candidatadas = Vaga.objects.filter(candidatos = aluno)
    return render(request, 'sistema/aluno_candidatadas.html', {'lista_vagas_candidatadas': lista_vagas_candidatadas,'aluno': aluno})

@login_required
@user_passes_test(is_professor)
def mostrar_candidatos(request, pk):
    try:
        vaga = Vaga.objects.get(pk = pk)
        if request.user == vaga.professor_responsavel.user:
            lista_candidatos = vaga.candidatos.all()
            return render(request, 'sistema/candidatos_list.html', {'lista_candidatos': lista_candidatos, 'vaga' : vaga})
        else:
            return redirect_to_login(request.get_full_path())
    except Vaga.DoesNotExist:
        raise Http404("Vaga não existe")
    except MultipleObjectsReturned:
        raise Http404("Devolveu mais de um objeto")

@login_required
@user_passes_test(is_professor)
def candidato_selecionado(request, pk_aluno, pk_vaga):
    try:
        vaga = Vaga.objects.get(pk = pk_vaga)
        aluno = Profile.objects.get(pk = pk_aluno)
        if not aluno.is_aluno:
            message.error(request,'Perfil seleccionado não é um aluno')
            return redirect(reverse('tela-inicial'))
        if not vaga.candidato_selecionado == None:
            message.error(request,'Já foi selecionado um aluno para esta vaga')
            return redirect(reverse('tela-inicial'))
        if request.user == vaga.professor_responsavel.user:
            vaga.candidato_selecionado = aluno
            vaga.save()
            messages.success(request,'Candidato %s selecionado com succeso' % vaga.candidato_selecionado)
            return redirect(reverse('tela-inicial'))
        else:
            return redirect_to_login(request.get_full_path())
    except Vaga.DoesNotExist:
        raise Http404("Vaga não existe")
    except Profile.DoesNotExist:
        raise Http404("Aluno não existe")
    except MultipleObjectsReturned:
        raise Http404("Devolveu mais de um objeto")

"""--------------------- CADASTRO E GESTAO USUARIOS ------------------------"""

@transaction.atomic
def create_aluno_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = AlunoProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = AlunoProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            user.profile.is_aluno = True
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse('tela-inicial'))
    else:
        user_form = UserCreationForm()
        profile_form = AlunoProfileForm()
    return render(request, 'registration/create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@transaction.atomic
def create_professor_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfessorProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.instance.is_active = False #O usuario professor ficará inativo até ser availado pelo coordinador
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfessorProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            user.profile.is_professor = True
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            messages.success(request,'O cadastro foi completo com sucesso, mas não poderá fazer login até o coordenador de seu departamento confirmar seu cadastro.')
            return redirect(reverse('tela-inicial'))
    else:
        user_form = UserCreationForm()
        profile_form = ProfessorProfileForm()
    return render(request, 'registration/create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
@user_passes_test(is_admin)
def create_coordenador_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = ProfessorProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = ProfessorProfileForm(request.POST, instance=user.profile)  # Reload the profile form with the profile instance
            user.profile.is_professor = True
            user.profile.chefe_departamento = True
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            messages.success(request,'Coordenador cadastrado com sucesso')
            return redirect(reverse('tela-inicial'))
    else:
        user_form = UserCreationForm()
        profile_form = ProfessorProfileForm()
    return render(request, 'registration/create_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
@user_passes_test(is_aluno)
def update_aluno_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = AlunoProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse('tela-inicial'))
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = AlunoProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
@user_passes_test(is_professor)
def update_professor_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfessorProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your profile was successfully updated!')
            return redirect(reverse('tela-inicial'))
        else:
            messages.error(request,'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfessorProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

class SolicitudesProfessores(ListView):
    model = Profile
    template_name = 'sistema/solicitudes_professores.html'
    @method_decorator(login_required)
    @method_decorator(user_passes_test(is_professor))
    @method_decorator(user_passes_test(is_chefe_departamento))
    def dispatch(self, *args, **kwargs):
        return super(SolicitudesProfessores, self).dispatch(*args, **kwargs)
    def get_queryset(self):
        return User.objects.filter(is_active = False, profile__is_professor = True, profile__departamento = self.request.user.profile.departamento)

@login_required
@user_passes_test(is_professor)
@user_passes_test(is_chefe_departamento)
def ativar_professor(request, pk):
    try:
        prof = Profile.objects.get(pk = pk)
        if request.user.profile.departamento == prof.departamento:
            prof.user.is_active = True
            prof.user.save()
            messages.success(request,'Professor %s ativado com succeso' %prof.user.first_name)
            return redirect(reverse('solicitudes-professores'))
        else:
            return redirect_to_login(request.get_full_path())
    except Profile.DoesNotExist:
        raise Http404("Professor não existe")
    except MultipleObjectsReturned:
        raise Http404("Devolveu mais de um objeto")

@login_required
@user_passes_test(is_admin)
def lista_coordenadores(request):
    lista_coordenadores = User.objects.filter(profile__chefe_departamento = True)
    return render(request, 'sistema/lista_coordenadores.html', {'lista_coordenadores': lista_coordenadores})

class Apagar_Perfil(SuccessMessageMixin,DeleteView):
    model = User
    success_url = reverse_lazy('tela-inicial')
    template_name = 'sistema/user_confirm_delete.html'
    success_message = "Perfil apagado com sucesso"
    def test_self_or_admin(self, request):
        return self.get_object() == request.user or request.user.profile.is_admin
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not self.test_self_or_admin(request):
            return redirect_to_login(request.get_full_path())
        return super(Apagar_Perfil, self).dispatch(
            request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Apagar_Perfil, self).delete(request, *args, **kwargs)
