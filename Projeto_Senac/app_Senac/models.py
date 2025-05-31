from django.db import models
from django.utils import timezone 
from django.core.validators import FileExtensionValidator

class Curso(models.Model):
    nome_curso = models.CharField(max_length=200, verbose_name="Nome do Curso")
    duracao_meses = models.IntegerField(verbose_name="Duração (meses)")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária (horas)")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor (R$)")
    # NOVO CAMPO DE IMAGEM:
    imagem_curso = models.ImageField(
        upload_to='cursos_imagens/', 
        verbose_name="Imagem do Curso",
        null=True, 
        blank=True,  
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])]
    )

    def __str__(self):
        return self.nome_curso

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    assunto = models.CharField(max_length=200, verbose_name="Assunto")
    mensagem = models.TextField(verbose_name="Mensagem")
    data_envio = models.DateTimeField(default=timezone.now, verbose_name="Data de Envio")
    lida = models.BooleanField(default=False, verbose_name="Lida") 

    def __str__(self):
        return f"Mensagem de {self.nome} - Assunto: {self.assunto}"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio'] 