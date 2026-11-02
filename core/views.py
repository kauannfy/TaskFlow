from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView,
)

from .forms import ProjetoForm, TarefaForm
from .models import Projeto, Tarefa


class DashboardView(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['total_projetos'] = Projeto.objects.count()
        ctx['total_tarefas'] = Tarefa.objects.count()
        ctx['tarefas_a_fazer'] = Tarefa.objects.filter(status='a_fazer').count()
        ctx['tarefas_em_andamento'] = Tarefa.objects.filter(status='em_andamento').count()
        ctx['tarefas_concluidas'] = Tarefa.objects.filter(status='concluida').count()
        ctx['projetos_recentes'] = Projeto.objects.all()[:5]
        ctx['tarefas_recentes'] = Tarefa.objects.select_related(
            'projeto', 'responsavel'
        ).order_by('-atualizado_em')[:5]
        ctx['tarefas_em_aberto'] = Tarefa.objects.filter(
            status__in=[Tarefa.Status.A_FAZER, Tarefa.Status.EM_ANDAMENTO]
        ).select_related('projeto').order_by('-criado_em')[:5]
        return ctx


# ---------- Projetos ----------
class ProjetoListView(ListView):
    model = Projeto

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['status_choices'] = Projeto.Status.choices
        ctx['f_status'] = self.request.GET.get('status', '')
        return ctx


class ProjetoDetailView(DetailView):
    model = Projeto

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tarefas = self.object.tarefas.select_related('responsavel')
        ctx['colunas'] = [
            (rotulo, tarefas.filter(status=valor)) for valor, rotulo in Tarefa.Status.choices
        ]
        return ctx


class ProjetoCreateView(SuccessMessageMixin, CreateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('core:projeto_lista')
    success_message = 'Projeto salvo com sucesso!'


class ProjetoUpdateView(SuccessMessageMixin, UpdateView):
    model = Projeto
    form_class = ProjetoForm
    success_url = reverse_lazy('core:projeto_lista')
    success_message = 'Projeto atualizado com sucesso!'


class ProjetoDeleteView(SuccessMessageMixin, DeleteView):
    model = Projeto
    success_url = reverse_lazy('core:projeto_lista')
    success_message = 'Projeto excluído com sucesso!'


# ---------- Tarefas ----------
class TarefaListView(ListView):
    model = Tarefa

    def get_queryset(self):
        qs = Tarefa.objects.select_related('projeto', 'responsavel')
        projeto = self.request.GET.get('projeto', '')
        status = self.request.GET.get('status', '')
        prioridade = self.request.GET.get('prioridade', '')
        if projeto.isdigit():
            qs = qs.filter(projeto_id=projeto)
        if status:
            qs = qs.filter(status=status)
        if prioridade:
            qs = qs.filter(prioridade=prioridade)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['projetos'] = Projeto.objects.all()
        ctx['status_choices'] = Tarefa.Status.choices
        ctx['prioridade_choices'] = Tarefa.Prioridade.choices
        ctx['f_projeto'] = self.request.GET.get('projeto', '')
        ctx['f_status'] = self.request.GET.get('status', '')
        ctx['f_prioridade'] = self.request.GET.get('prioridade', '')
        return ctx


class TarefaSucessoMixin:
    """Depois de salvar/excluir, volta para a página do projeto da tarefa."""
    def get_success_url(self):
        return reverse('core:projeto_detalhe', args=[self.object.projeto_id])


class TarefaCreateView(TarefaSucessoMixin, SuccessMessageMixin, CreateView):
    model = Tarefa
    form_class = TarefaForm
    success_message = 'Tarefa criada com sucesso!'

    def get_initial(self):
        initial = super().get_initial()
        projeto = self.request.GET.get('projeto')
        if projeto:
            initial['projeto'] = projeto
        return initial


class TarefaUpdateView(TarefaSucessoMixin, SuccessMessageMixin, UpdateView):
    model = Tarefa
    form_class = TarefaForm
    success_message = 'Tarefa atualizada com sucesso!'


class TarefaDeleteView(TarefaSucessoMixin, SuccessMessageMixin, DeleteView):
    model = Tarefa
    success_message = 'Tarefa excluída com sucesso!'