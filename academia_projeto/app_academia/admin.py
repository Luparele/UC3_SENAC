from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Produto, ContatoMensagem, ClienteProfile 

class ClienteProfileInline(admin.StackedInline):
    model = ClienteProfile
    can_delete = False
    verbose_name_plural = 'Perfis de Cliente'
    fk_name = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (ClienteProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_telefone_contato')

    def get_telefone_contato(self, instance):
        try:
            return instance.cliente_profile.telefone_contato
        except ClienteProfile.DoesNotExist:
            return "N/A"
    get_telefone_contato.short_description = 'Telefone de Contato'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Produto)
admin.site.register(ContatoMensagem)