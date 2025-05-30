from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Produto, ContatoMensagem, ClienteProfile 
from .forms import CustomUserCreationForm, ContatoForm, ProdutoForm, CustomLoginForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

def em_construcao_view(request):
    context = {
        'titulo_pagina': 'Página em Construção'
    }
    return render(request, 'app_academia/em_construcao.html', context)

def home_view(request):
    return render(request, 'app_academia/home.html')

@staff_member_required
def pesquisa_clientes_view(request): 
    query = request.GET.get('q', '')
    show_all_param = request.GET.get('show_all', 'false').lower() == 'true'

    usuarios_encontrados = User.objects.none()
    is_showing_all = False 

    if show_all_param:
        usuarios_encontrados = User.objects.all().order_by('username').select_related('cliente_profile')
        is_showing_all = True
    elif query:
        usuarios_encontrados = User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(cliente_profile__telefone_contato__icontains=query) 
        ).distinct().select_related('cliente_profile')

    context = {
        'query': query,
        'usuarios': usuarios_encontrados,
        'is_showing_all': is_showing_all,
        'titulo_pagina': 'Pesquisa de Usuários (Admin)'
    }
    return render(request, 'app_academia/pesquisa_clientes.html', context)


def cadastro_usuario_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, 'Cadastro realizado com sucesso! Você já está logado.')
            return redirect('app_academia:home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label if field != '__all__' else ''}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'app_academia/usuarios.html', {'form': form, 'titulo_pagina': 'Cadastre-se'})

@login_required 
def usuarios_view(request):
    return redirect('app_academia:cadastro_usuario')


def produtos_view(request):
    produtos = Produto.objects.all()
    return render(request, 'app_academia/produtos.html', {'produtos': produtos})


def contato_view(request):
    form_contato = None 

    if request.user.is_authenticated:
        if request.method == 'POST':
            form_contato = ContatoForm(request.POST)
            if form_contato.is_valid():
                contato = form_contato.save(commit=False)
                contato.usuario = request.user 
                contato.save()
                messages.success(request, 'Sua mensagem foi enviada com sucesso!')
                return redirect('app_academia:contato') 
            else:
                messages.error(request, 'Ocorreu um erro ao enviar sua mensagem. Verifique os dados.')
        else: 
            form_contato = ContatoForm()
    numero_whatsapp = "5521976658035" 
    nome_display_whatsapp = "Visitante"
    if request.user.is_authenticated:
        nome_display_whatsapp = request.user.first_name if request.user.first_name else request.user.username

    mensagem_whatsapp_prefill = f"Olá! Gostaria de mais informações sobre a academia. (Enviado por: {nome_display_whatsapp})"
    link_whatsapp = f"https://wa.me/{numero_whatsapp}?text={mensagem_whatsapp_prefill.replace(' ', '%20')}"

    context = {
        'form': form_contato,
        'link_whatsapp': link_whatsapp,
        'titulo_pagina': 'Fale Conosco'
    }
    return render(request, 'app_academia/contato.html', context)

def sobre_view(request):
    mapa_embed_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3675.188435989201!2d-43.17492808503327!3d-22.90684688501199!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x997f58a6a00001%3A0x7d89ce1811a4d70c!2sMaracan%C3%A3!5e0!3m2!1spt-BR!2sbr!4v1620832984751!5m2!1spt-BR!2sbr" # EXEMPLO
    context = {
        'mapa_embed_url': mapa_embed_url
    }
    return render(request, 'app_academia/sobre.html', context)

@staff_member_required
def cadastrar_produto_view(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto_salvo = form.save()
            messages.success(request, f"Produto '{produto_salvo.nome_produto}' cadastrado com sucesso!")
            return redirect('app_academia:produtos')
        else:
            messages.error(request, "Erro ao cadastrar o produto. Por favor, verifique os dados informados.")
    else:
        form = ProdutoForm()

        produtos_cadastrados = Produto.objects.all().order_by('-id')

    context = {
        'form': form,
        'produtos_cadastrados': produtos_cadastrados,
        'titulo_pagina': 'Cadastrar e Gerenciar Produtos (Admin)'
    }
    return render(request, 'app_academia/cadastrar_produto.html', context)

@staff_member_required
@require_POST # Garante que a deleção só ocorra via POST
def apagar_produto_view(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    try:
        nome_produto = produto.nome_produto
        
        if produto.imagem_produto:
            produto.imagem_produto.delete(save=False) 

        produto.delete() 
        messages.success(request, f"Produto '{nome_produto}' apagado com sucesso.")
    except Exception as e:
        messages.error(request, f"Erro ao tentar apagar o produto '{produto.nome_produto}': {str(e)}")
    
    return redirect('app_academia:cadastrar_produto')

@staff_member_required 
def ver_mensagens_contato_view(request):
    mensagens_list = ContatoMensagem.objects.all().order_by('-data_envio').select_related('usuario')
    
    paginator = Paginator(mensagens_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'titulo_pagina': 'Mensagens de Contato Recebidas (Admin)'
    }
    return render(request, 'app_academia/ver_mensagens_contato.html', context)

@staff_member_required
@require_POST 
def apagar_mensagem_contato_view(request, mensagem_id):
    mensagem = get_object_or_404(ContatoMensagem, id=mensagem_id)
    try:
        usuario_remetente = str(mensagem.usuario) if mensagem.usuario else "Visitante Anônimo"
        data_envio_msg = mensagem.data_envio.strftime('%d/%m/%Y %H:%M')
        
        mensagem.delete()
        messages.success(request, f"A mensagem de '{usuario_remetente}' (enviada em {data_envio_msg}) foi apagada com sucesso.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao tentar apagar a mensagem: {str(e)}")
    
    return redirect('app_academia:ver_mensagens_contato')

def planos_view(request):
    plans_data = [
        {
            'name': 'Básico',
            'price': '79,90',
            'price_period': '/mês',
            'features': [
                'Acesso à área de musculação',
                'Horário limitado (ex: 6h-18h)',
                '1 Avaliação física inicial',
                'Armário rotativo',
            ],
            'button_text': 'Assinar Básico',
            'button_class': 'btn-outline-primary',
            'is_featured': False,
            'header_class': 'bg-light text-dark' 
        },
        {
            'name': 'Deluxe', 
            'price': '129,90',
            'price_period': '/mês',
            'features': [
                'Acesso total e irrestrito 24/7',
                'Todas as aulas de grupo inclusas',
                'Aulas especiais (Yoga, Pilates, Spinning)',
                'Avaliação física trimestral',
                'Acompanhamento nutricional básico',
                'Armário individual grande',
                'Toalha e água mineral'
            ],
            'button_text': 'Assinar Deluxe',
            'button_class': 'btn-primary', 
            'is_featured': True,
            'header_class': 'bg-primary text-white', 
            'badge_text': 'Mais Popular'
        },
        {
            'name': 'Premium', 
            'price': '99,90',
            'price_period': '/mês',
            'features': [
                'Acesso completo à musculação e cárdio',
                'Aulas de grupo (manhã e noite)',
                'Avaliação física semestral',
                'Armário individual médio',
            ],
            'button_text': 'Assinar Premium',
            'button_class': 'btn-outline-primary',
            'is_featured': False,
            'header_class': 'bg-light text-dark'
        }
    ]
    context = {
        'titulo_pagina': 'Nossos Planos',
        'plans': plans_data
    }
    return render(request, 'app_academia/planos.html', context)