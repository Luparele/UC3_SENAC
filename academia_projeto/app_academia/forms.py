from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from .models import ContatoMensagem, ClienteProfile, Produto
from django.utils.translation import gettext_lazy as _

class CustomUserCreationForm(UserCreationForm):
    nome_completo = forms.CharField(
        label=_("Nome completo"), 
        max_length=100,
        help_text=_('Seu nome completo.')
    )
    telefone_contato = forms.CharField(
        label=_("Telefone de contato"),
        max_length=15,
        required=False,
        help_text=_('(Opcional)')
    )
    email = forms.EmailField(
        label=_("Endereço de e-mail"),
        required=True,
        help_text=_('Obrigatório. Será usado para login e notificações.')
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizando campos herdados do UserCreationForm
        if 'username' in self.fields:
            self.fields['username'].label = _("Nome de usuário")
            self.fields['username'].help_text = _('Obrigatório. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.')
        if 'password1' in self.fields:
            self.fields['password1'].label = _("Senha")
        if 'password2' in self.fields:
            self.fields['password2'].label = _("Confirmação de senha")
            self.fields['password2'].help_text = _('Digite a mesma senha como anteriormente, para verificação.')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "nome_completo", "telefone_contato")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["nome_completo"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            ClienteProfile.objects.get_or_create(
                user=user,
                defaults={'telefone_contato': self.cleaned_data.get("telefone_contato")}
            )
        return user


class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContatoMensagem
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Deixe sua mensagem aqui...'}),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'valor', 'imagem_produto']
        widgets = {
            'nome_produto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Whey Protein Concentrado'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Ex: 99.90'}),
            'imagem_produto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_produto': 'Nome do Produto',
            'valor': 'Valor (R$)',
            'imagem_produto': 'Imagem do Produto (Opcional)',
        }
        help_texts = {
            'valor': 'Use ponto como separador decimal, ex: 75.50',
        }

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Usuário ou Email"),
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Digite seu nome de usuário ou email',
            'autofocus': True
        })
    )
    password = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Digite sua senha'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)