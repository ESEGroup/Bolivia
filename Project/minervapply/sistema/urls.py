from django.conf.urls import url, include
from sistema import views

urlpatterns=[
    url(r'^home/$', views.TelaInicial.as_view(), name = 'tela-inicial'),
    url(r'^atualizar_professor/$', views.update_professor_profile, name='atualizar_professor'),
    url(r'^cadastrar_professor/$', views.create_professor_view, name='cadastrar-professor'),
    url(r'^atualizar_aluno/$', views.update_aluno_profile, name='atualizar_aluno'),
    url(r'^cadastrar_aluno/$', views.create_aluno_view, name='cadastrar-aluno'),
    url(r'^professor_logado/$', views.ProfessorLogado.as_view(), name = 'professor-logado'),
    url(r'^professor_logado/add/$', views.Criar_Vaga.as_view(), name='adicionar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/$', views.Atualizar_Vaga.as_view(), name='atualizar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/delete/$', views.Apagar_Vaga.as_view(), name='apagar-vaga'),
    url(r'^professor_logado/solicitudes_professores/$', views.SolicitudesProfessores.as_view(), name = 'solicitudes-professores'),
    url(r'^professor_logado/ativar_professor/(?P<pk>[0-9]+)/$', views.ativar_professor, name = 'ativar-professor'),
    url(r'^professor_logado/mostrar_candidatos/(?P<pk>[0-9]+)/$', views.mostrar_candidatos, name = 'mostrar_candidatos'),

    url(r'^candidatarse/(?P<pk>[0-9]+)/$', views.candidatarse, name = 'candidatarse'),


    # url(r'^pesquisar_aluno(?P<pk>[0-9]+)/$', views.TelaInicial.as_view(), name = 'tela-inicial'),
]
