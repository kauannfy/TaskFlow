from django.conf import settings
from django.db import models


class Projeto(models.Model):
    class Status(models.TextChoices):
        PLANEJADO = 'planejado', 'Planejado'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        CONCLUIDO = 'concluido', 'Concluído'

    nome = models.CharField('Nome', max_length=120)
    descricao = models.TextField('Descrição', blank=True)
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.PLANEJADO)
    data_inicio = models.DateField('Data de início', null=True, blank=True)
    data_fim_prevista = models.DateField('Término previsto', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

    def percentual_concluido(self):
        total = self.tarefas.count()
        if total == 0:
            return 0
        concluidas = self.tarefas.filter(status='concluida').count()
        return round(concluidas * 100 / total)



class Tarefa(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = 'baixa', 'Baixa'
        MEDIA = 'media', 'Média'
        ALTA = 'alta', 'Alta'

    class Status(models.TextChoices):
        A_FAZER = 'a_fazer', 'A fazer'
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        CONCLUIDA = 'concluida', 'Concluída'

    projeto = models.ForeignKey(Projeto, verbose_name='Projeto', on_delete=models.CASCADE, related_name='tarefas')
    titulo = models.CharField('Título', max_length=150)
    descricao = models.TextField('Descrição', blank=True)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Responsável',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas_responsavel',
    )
    prioridade = models.CharField('Prioridade', max_length=10, choices=Prioridade.choices, default=Prioridade.MEDIA)
    status = models.CharField('Status', max_length=20, choices=Status.choices, default=Status.A_FAZER)
    prazo = models.DateField('Prazo', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo

    @property
    def nome_responsavel(self):
        if not self.responsavel:
            return 'Sem responsável'
        return self.responsavel.get_full_name() or self.responsavel.get_username()