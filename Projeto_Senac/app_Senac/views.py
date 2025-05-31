# app_Senac/views.py
from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Curso, MensagemContato 
from .forms import CursoForm, MensagemContatoForm, CustomUserCreationForm 

def politica_de_privacidade_view(request):
    context = {
        'page_title': 'Política de Privacidade'
    }
    return render(request, 'app_Senac/politica_de_privacidade.html', context)

def detalhe_curso_view(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    context = {
        'curso': curso,
        'page_title': curso.nome_curso # Para o título da aba do navegador
    }
    return render(request, 'app_Senac/detalhe_curso.html', context)

# NOVA VIEW PARA PÁGINA "TERMOS DE USO":
def termos_de_uso_view(request):
    context = {
        'page_title': 'Termos de Uso'
    }
    return render(request, 'app_Senac/termos_de_uso.html', context)

def em_construcao_view(request):
    context = {
        'page_title': 'Página em Construção' 
    }
    return render(request, 'app_Senac/em_construcao.html', context)

def home_view(request):
    return render(request, 'app_Senac/home.html')

def sobre_view(request):
    return render(request, 'app_Senac/sobre.html')

def cursos_view(request):
    todos_cursos = Curso.objects.all().order_by('nome_curso')
    context = {
        'cursos': todos_cursos,
        'page_title': 'Nossos Cursos'
    }
    return render(request, 'app_Senac/cursos.html', context)

def excluir_curso_view(request, curso_id):
    curso_para_excluir = get_object_or_404(Curso, id=curso_id)
    
    if request.method == 'POST': 
        nome_curso = curso_para_excluir.nome_curso
        curso_para_excluir.delete()
        messages.success(request, f"O curso '{nome_curso}' foi excluído com sucesso.")
        return redirect('cadastro_curso') 
    else:
        messages.warning(request, "Ação de exclusão inválida. Use o botão na página de gerenciamento.")
        return redirect('cadastro_curso')

def contato_view(request):
    if request.method == 'POST':
        form = MensagemContatoForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.')
            return redirect('contato') 
        else:
            messages.error(request, 'Houve um erro no formulário. Por favor, verifique os campos destacados.')
    else:
        form = MensagemContatoForm()

    context = {
        'form': form,
        'page_title': 'Entre em Contato'
    }
    return render(request, 'app_Senac/contato.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Bem-vindo(a) de volta, {user.get_username()}!')
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('home')
            else: 
                messages.error(request, 'Login ou senha inválidos.')
        else:
            messages.error(request, 'Login ou senha inválidos. Por favor, tente novamente.')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
        'page_title': 'Acessar sua Conta'
    }
    return render(request, 'app_Senac/login.html', context)

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Você saiu com sucesso da sua conta.')
    return redirect('home')

def cadastro_view(request):
    if request.user.is_authenticated: 
        return redirect('home')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user) 
            messages.success(request, f'Cadastro realizado com sucesso, {user.username}! Você já está logado.')
            return redirect('home') 
        else:
            messages.error(request, 'Houve um erro no seu cadastro. Por favor, verifique os campos e tente novamente.')
    else:
        form = CustomUserCreationForm() 
    
    context = {
        'form': form,
        'page_title': 'Crie sua Conta'
    }
    return render(request, 'app_Senac/cadastro.html', context)


def pesquisa_cliente_view(request):
    query = request.GET.get('q', '') 

    if query:
        lista_clientes = User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).distinct().order_by('username')
        page_subtitle = f"Resultados da busca por: \"{query}\""
    else:
        lista_clientes = User.objects.all().order_by('username')
        page_subtitle = "Todos os Clientes Cadastrados"

    context = {
        'clientes': lista_clientes,
        'query': query, 
        'page_title': 'Gerenciamento de Clientes',
        'page_subtitle': page_subtitle
    }
    return render(request, 'app_Senac/pesquisa_cliente.html', context)

def cadastro_curso_view(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            messages.success(request, f"Curso '{form.cleaned_data.get('nome_curso')}' salvo com sucesso!")
            return redirect('cadastro_curso') 
        else:
            messages.error(request, "Erro ao salvar o curso. Verifique os campos do formulário.")
    else:
        form = CursoForm() 

    cursos_cadastrados = Curso.objects.all().order_by('-id')
    context = {
        'form': form,
        'cursos': cursos_cadastrados,
        'page_title': 'Cadastro e Gerenciamento de Cursos'
    }
    return render(request, 'app_Senac/cadastro_curso.html', context)

def mensagens_view(request):
    lista_de_mensagens_contato = MensagemContato.objects.all() 
    context = {
        'lista_mensagens_contato': lista_de_mensagens_contato, 
        'page_title': 'Mensagens Recebidas'
    }
    return render(request, 'app_Senac/mensagens.html', context)

def excluir_mensagem_view(request, mensagem_id):
    mensagem_para_excluir = get_object_or_404(MensagemContato, id=mensagem_id)
    
    if request.method == 'POST': 
        nome_remetente = mensagem_para_excluir.nome
        assunto_msg = mensagem_para_excluir.assunto
        mensagem_para_excluir.delete()
        messages.success(request, f"Mensagem de '{nome_remetente}' sobre '{assunto_msg}' foi excluída com sucesso.")
        return redirect('mensagens') 
    else:
        messages.warning(request, "Ação de exclusão inválida.")
        return redirect('mensagens')