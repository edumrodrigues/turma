from django.conf.urls import *
from django.conf import settings
from turmaApp import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', views.TurmaListView.as_view()),

    url(r'^turma/lista/$', views.TurmaListView.as_view(), name='lista_turma'),
    url(r'^turma/cadastro/$', views.TurmaCreateView.as_view(), name='cadastro_turma'),
    url(r'^turma/(?P<pk>\d+)/edita/$', views.TurmaUpdateView.as_view(), name='edita_turma'),    
    url(r'^turma/(?P<pk>\d+)/deleta/$', views.TurmaDeleteView.as_view(), name='deleta_turma'),
    url(r'^pesquisa_turma/$', views.TurmaSearchView.as_view(), name='pesquisa_turma'),
    #=============================================================================================
    url(r'^aluno/lista/$', views.AlunoListView.as_view(), name='lista_aluno'),
    url(r'^aluno/cadastro/$', views.AlunoCreateView.as_view(), name='cadastro_aluno'),
    url(r'^aluno/(?P<pk>\d+)/edita/$', views.AlunoUpdateView.as_view(), name='edita_aluno'),    
    url(r'^aluno/(?P<pk>\d+)/deleta/$', views.AlunoDeleteView.as_view(), name='deleta_aluno'),
    url(r'^pesquisa_aluno/$', views.AlunoSearchView.as_view(), name='pesquisa_aluno'),
    #=============================================================================================
    url(r'^professor/lista$', views.ProfessorListView.as_view(), name='lista_professor'),
    url(r'^professor/cadastro/$', views.ProfessorCreateView.as_view(), name='cadastro_professor'),
    url(r'^professor/(?P<pk>\d+)/edita/$', views.ProfessorUpdateView.as_view(), name='edita_professor'),    
    url(r'^professor/(?P<pk>\d+)/deleta/$', views.ProfessorDeleteView.as_view(), name='deleta_professor'),
    url(r'^pesquisa_professor/$', views.ProfessorSearchView.as_view(), name='pesquisa_professor'),

    url(r'saved/$', TemplateView.as_view(template_name='turmaApp/saved.html'), name='saved'),
    url(r'sobre/$', TemplateView.as_view(template_name='turmaApp/sobre.html'), name='sobre'),
    url(r'^turma/lista/(?P<pk>\d+)/detalhe/$', views.TurmaDetailView.as_view(), name='detalhe_turma'),
)
