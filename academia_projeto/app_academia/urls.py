from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from .forms import CustomLoginForm

app_name = 'app_academia'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='app_academia/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app_academia:home'), name='logout'),
    path('cadastro/', views.cadastro_usuario_view, name='cadastro_usuario'),
    path('usuarios/', views.usuarios_view, name='usuarios'), 
    path('produtos/', views.produtos_view, name='produtos'),
    path('contato/', views.contato_view, name='contato'),
    path('sobre/', views.sobre_view, name='sobre'),
    path('planos/', views.planos_view, name='planos'),
    path('gerenciamento/pesquisa-clientes/', views.pesquisa_clientes_view, name='pesquisa_clientes'),
    path('gerenciamento/cadastrar-produto/', views.cadastrar_produto_view, name='cadastrar_produto'),
    path('gerenciamento/mensagens-contato/', views.ver_mensagens_contato_view, name='ver_mensagens_contato'),
    path('gerenciamento/mensagens-contato/apagar/<int:mensagem_id>/', views.apagar_mensagem_contato_view, name='apagar_mensagem_contato'),
    path('gerenciamento/produtos/apagar/<int:produto_id>/', views.apagar_produto_view, name='apagar_produto'),
    path('em-construcao/', views.em_construcao_view, name='em_construcao'),
]