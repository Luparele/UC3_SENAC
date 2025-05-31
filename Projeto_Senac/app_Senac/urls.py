from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('contato/', views.contato_view, name='contato'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('gerenciar-clientes/', views.pesquisa_cliente_view, name='pesquisa_cliente'),
    path('gerenciar-cursos/', views.cadastro_curso_view, name='cadastro_curso'),
    path('mensagens-recebidas/', views.mensagens_view, name='mensagens'),
    path('mensagens/excluir/<int:mensagem_id>/', views.excluir_mensagem_view, name='excluir_mensagem'),
    path('gerenciar-cursos/excluir/<int:curso_id>/', views.excluir_curso_view, name='excluir_curso'),
    path('logout/', views.logout_view, name='logout'),
    path('em-construcao/', views.em_construcao_view, name='em_construcao'),
    path('politica-de-privacidade/', views.politica_de_privacidade_view, name='politica_privacidade'),
    path('termos-de-uso/', views.termos_de_uso_view, name='termos_uso'),
    path('cursos/<int:curso_id>/', views.detalhe_curso_view, name='detalhe_curso'),
]