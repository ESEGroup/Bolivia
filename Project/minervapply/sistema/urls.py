from django.conf.urls import url, include
from sistema import views

urlpatterns=[
    url(r'^home/$', views.TelaInicial.as_view(), name = 'tela-inicial'),
    url(r'^atualizar_professor/$', views.update_profile, name='atualizar_professor'),
    url(r'^cadastrar_professor/$', views.create_user_view, name='cadastrar-professor'),
    url(r'^professor_logado/$', views.ProfessorLogado.as_view(), name = 'professor-logado'),
    url(r'^professor_logado/add/$', views.Criar_Vaga.as_view(), name='adicionar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/$', views.Atualizar_Vaga.as_view(), name='atualizar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/delete/$', views.Apagar_Vaga.as_view(), name='apagar-vaga'),
]
