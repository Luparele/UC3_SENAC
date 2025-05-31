from django.contrib import admin
from .models import Curso, MensagemContato
from django.utils.html import format_html

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome_curso', 'duracao_meses', 'carga_horaria', 'valor', 'display_imagem_curso')
    search_fields = ('nome_curso',)
    list_filter = ('duracao_meses', 'valor')
    readonly_fields = ('preview_imagem_curso',) 

    def display_imagem_curso(self, obj):
        if obj.imagem_curso:
            return format_html('<img src="{}" width="70" height="50" style="object-fit:cover;" />', obj.imagem_curso.url)
        return "Sem imagem"
    display_imagem_curso.short_description = 'Imagem'

    def preview_imagem_curso(self, obj):
        if obj.imagem_curso:
            return format_html('<img src="{}" width="150" style="max-height:150px; object-fit:contain;" />', obj.imagem_curso.url)
        return "(Nenhuma imagem)"
    preview_imagem_curso.short_description = 'Preview da Imagem Atual'

    fieldsets = (
        (None, {
            'fields': ('nome_curso', 'duracao_meses', 'carga_horaria', 'valor')
        }),
        ('Imagem do Curso', {
            'fields': ('imagem_curso', 'preview_imagem_curso') 
        }),
    )

admin.site.register(Curso, CursoAdmin)

@admin.register(MensagemContato) 
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'data_envio', 'lida')
    list_filter = ('lida', 'data_envio')
    search_fields = ('nome', 'email', 'assunto', 'mensagem')
    readonly_fields = ('nome', 'email', 'assunto', 'mensagem', 'data_envio') 
    list_per_page = 20 

    def marcar_como_lida(self, request, queryset):
        queryset.update(lida=True)
    marcar_como_lida.short_description = "Marcar selecionadas como lidas"

    def marcar_como_nao_lida(self, request, queryset):
        queryset.update(lida=False)
    marcar_como_nao_lida.short_description = "Marcar selecionadas como não lidas"

    actions = [marcar_como_lida, marcar_como_nao_lida]

    
    def has_add_permission(self, request):
        return False