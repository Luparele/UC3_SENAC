# app_Senac/forms.py
from django import forms
from .models import Curso, MensagemContato
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'duracao_meses', 'carga_horaria', 'valor', 'imagem_curso']
        widgets = {
            'nome_curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Python para Análise de Dados'}),
            'duracao_meses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 3'}),
            'carga_horaria': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 60'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 499.90'}),
            'imagem_curso': forms.ClearableFileInput(attrs={'class': 'form-control-file'}), 
        }
        labels = {
            'nome_curso': 'Nome do Curso',
            'duracao_meses': 'Duração (em meses)',
            'carga_horaria': 'Carga Horária (total de horas)',
            'valor': 'Valor do Curso (R$)',
            'imagem_curso': 'Imagem de Capa do Curso',
        }
        help_texts = {
            'valor': 'Use ponto como separador decimal. Ex: 150.00',
            'imagem_curso': 'Envie uma imagem representativa para o curso (opcional).'
        }

class MensagemContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ['nome', 'email', 'assunto', 'mensagem'] 
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@exemplo.com'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto da mensagem'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Digite sua mensagem aqui...'}),
        }
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu Melhor E-mail',
            'assunto': 'Assunto',
            'mensagem': 'Sua Mensagem',
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@exemplo.com'}),
        label="E-mail"
    )
    first_name = forms.CharField(
        required=True, 
        max_length=30, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu primeiro nome'}),
        label="Nome"
    )
    last_name = forms.CharField(
        required=True, 
        max_length=150, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu sobrenome'}),
        label="Sobrenome"
    )
    telefone = forms.CharField(
        required=False, 
        max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX (Opcional)'}),
        label="Telefone (Opcional)"
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'telefone')
        labels = {
            'username': 'Login (Nome de Usuário)',
        }
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escolha um nome de usuário'}),
        }


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save() 
        return user
    
