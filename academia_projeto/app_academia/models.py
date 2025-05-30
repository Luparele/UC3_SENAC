from django.db import models
from django.contrib.auth.models import User

class ClienteProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente_profile')
    telefone_contato = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_produto = models.ImageField(upload_to='produtos_imagens/', blank=True, null=True)

    def __str__(self):
        return self.nome_produto

class ContatoMensagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.usuario:
            return f"Mensagem de {self.usuario.username} em {self.data_envio.strftime('%d/%m/%Y %H:%M')}"
        return f"Mensagem anônima em {self.data_envio.strftime('%d/%m/%Y %H:%M')}"