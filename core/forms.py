from django import forms
from .models import Projeto, Tarefa


class EstiloMixin:
    """Aplica a classe CSS 'campo' em todos os inputs."""
    required_css_class = 'required-field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.setdefault('class', 'campo')


class ProjetoForm(EstiloMixin, forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'status', 'data_inicio', 'data_fim_prevista']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'data_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'data_fim_prevista': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean(self):
        dados = super().clean()
        inicio = dados.get('data_inicio')
        fim = dados.get('data_fim_prevista')
        if inicio and fim and fim < inicio:
            self.add_error('data_fim_prevista', 'O término não pode ser anterior ao início.')
        return dados


class TarefaForm(EstiloMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projeto'].empty_label = 'Selecione um projeto'
        self.fields['responsavel'].empty_label = 'Selecione um responsável'
        self.fields['responsavel'].help_text = 'Opcional.'

    class Meta:
        model = Tarefa
        fields = ['projeto', 'titulo', 'descricao', 'responsavel', 'prioridade', 'status', 'prazo']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'prazo': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }