from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^(?P<nome_professor>\w+)/$', views.professor_logado, name = 'professor_logado'),
    url(r'^(?P<nome_professor>\w+)/formulario/$', views.formulario_vaga, name = 'formulario'),
]
