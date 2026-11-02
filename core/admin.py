from django.contrib import admin
from .models import Projeto, Tarefa


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status', 'data_inicio', 'data_fim_prevista', 'criado_em')
    list_filter = ('status',)
    search_fields = ('nome', 'descricao')


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel', 'prioridade', 'status', 'prazo')
    list_filter = ('status', 'prioridade', 'projeto')
    search_fields = ('titulo', 'descricao')