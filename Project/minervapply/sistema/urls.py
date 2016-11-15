from django.conf.urls import url, include
from sistema import views

urlpatterns=[
    url(r'^(?P<nome_professor>\w+)/$', views.professor_logado, name = 'professor-logado'),
    #url(r'', views.escolha_professor, name='escolha-professor'),
    url(r'^(?P<nome_professor>\w+)/add/$', views.Criar_Vaga.as_view(), name='adicionar-vaga'),
    url(r'^(?P<nome_professor>\w+)/(?P<pk>[0-9]+)/$', views.Atualizar_Vaga.as_view(), name='atualizar-vaga'),
    url(r'^(?P<nome_professor>\w+)/(?P<pk>[0-9]+)/delete/$', views.Apagar_Vaga.as_view(), name='apagar-vaga'),
]
