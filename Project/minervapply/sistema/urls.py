from django.conf.urls import url, include
from sistema import views

urlpatterns=[
    url(r'^home/$', views.TelaInicial.as_view(), name = 'tela-inicial'),
    url(r'^professor_logado/$', views.ProfessorLogado.as_view(), name = 'professor-logado'),
    url(r'^professor_logado/add/$', views.Criar_Vaga.as_view(), name='adicionar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/$', views.Atualizar_Vaga.as_view(), name='atualizar-vaga'),
    url(r'^professor_logado/(?P<pk>[0-9]+)/delete/$', views.Apagar_Vaga.as_view(), name='apagar-vaga'),
]
