from django.test import TestCase
from django.urls import reverse

from .models import Projeto, Tarefa


class ProjetoWorkflowTests(TestCase):
    def setUp(self):
        self.projeto = Projeto.objects.create(
            nome='Projeto de teste',
            descricao='Descrição do projeto',
        )

    def test_lista_projetos_exibe_projeto_e_link_de_cadastro(self):
        response = self.client.get(reverse('core:projeto_lista'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.projeto.nome)
        self.assertContains(response, reverse('core:projeto_novo'))

    def test_cadastro_de_projeto_valido_exibe_mensagem(self):
        response = self.client.post(
            reverse('core:projeto_novo'),
            {'nome': 'Novo projeto', 'descricao': '', 'status': Projeto.Status.PLANEJADO},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse('core:projeto_lista'))
        self.assertTrue(Projeto.objects.filter(nome='Novo projeto').exists())
        self.assertContains(response, 'Projeto salvo com sucesso!')

    def test_cadastro_de_projeto_invalido_nao_salva(self):
        response = self.client.post(reverse('core:projeto_novo'), {'nome': ''})

        self.assertEqual(response.status_code, 200)
        self.assertIn('nome', response.context['form'].errors)
        self.assertEqual(Projeto.objects.count(), 1)

    def test_edicao_de_projeto_atualiza_dados_e_exibe_mensagem(self):
        response = self.client.post(
            reverse('core:projeto_editar', args=[self.projeto.pk]),
            {
                'nome': 'Projeto atualizado',
                'descricao': 'Nova descrição',
                'status': Projeto.Status.EM_ANDAMENTO,
            },
            follow=True,
        )

        self.projeto.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse('core:projeto_lista'))
        self.assertEqual(self.projeto.nome, 'Projeto atualizado')
        self.assertContains(response, 'Projeto atualizado com sucesso!')

    def test_detalhe_lista_tarefas_por_status_e_estado_vazio(self):
        tarefa = Tarefa.objects.create(
            projeto=self.projeto,
            titulo='Tarefa em andamento',
            status=Tarefa.Status.EM_ANDAMENTO,
        )

        response = self.client.get(reverse('core:projeto_detalhe', args=[self.projeto.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, tarefa.titulo)
        self.assertContains(response, 'Em andamento')
        self.assertContains(response, reverse('core:tarefa_editar', args=[tarefa.pk]))

        tarefa.delete()
        empty_response = self.client.get(reverse('core:projeto_detalhe', args=[self.projeto.pk]))
        self.assertContains(empty_response, 'Este projeto ainda não possui tarefas')

    def test_exclusao_de_projeto_exige_post_e_exibe_mensagem(self):
        url = reverse('core:projeto_excluir', args=[self.projeto.pk])
        confirmation = self.client.get(url)

        self.assertEqual(confirmation.status_code, 200)
        self.assertContains(confirmation, 'method="post"')
        self.assertTrue(Projeto.objects.filter(pk=self.projeto.pk).exists())

        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], reverse('core:projeto_lista'))
        self.assertFalse(Projeto.objects.filter(pk=self.projeto.pk).exists())
        self.assertContains(response, 'Projeto excluído com sucesso!')

    def test_exclusao_de_projeto_remove_tarefas_relacionadas(self):
        tarefa = Tarefa.objects.create(projeto=self.projeto, titulo='Tarefa vinculada')

        self.client.post(reverse('core:projeto_excluir', args=[self.projeto.pk]))

        self.assertFalse(Tarefa.objects.filter(pk=tarefa.pk).exists())


class TarefaWorkflowTests(TestCase):
    def setUp(self):
        self.projeto = Projeto.objects.create(nome='Projeto de tarefas')
        self.outro_projeto = Projeto.objects.create(nome='Outro projeto')
        self.tarefa = Tarefa.objects.create(
            projeto=self.projeto,
            titulo='Tarefa de teste',
            prioridade=Tarefa.Prioridade.MEDIA,
            status=Tarefa.Status.A_FAZER,
        )

    def test_lista_tarefas_exibe_dados_e_acoes(self):
        response = self.client.get(reverse('core:tarefa_lista'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tarefa.titulo)
        self.assertContains(response, self.projeto.nome)
        self.assertContains(response, reverse('core:tarefa_editar', args=[self.tarefa.pk]))
        self.assertContains(response, reverse('core:tarefa_excluir', args=[self.tarefa.pk]))

    def test_filtros_de_tarefas_por_projeto_status_e_prioridade(self):
        outra_tarefa = Tarefa.objects.create(
            projeto=self.outro_projeto,
            titulo='Tarefa de outro projeto',
            prioridade=Tarefa.Prioridade.ALTA,
            status=Tarefa.Status.CONCLUIDA,
        )
        response = self.client.get(
            reverse('core:tarefa_lista'),
            {
                'projeto': self.projeto.pk,
                'status': Tarefa.Status.A_FAZER,
                'prioridade': Tarefa.Prioridade.MEDIA,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['object_list']), [self.tarefa])
        self.assertNotContains(response, outra_tarefa.titulo)
        self.assertEqual(response.context['f_projeto'], str(self.projeto.pk))

    def test_cadastro_de_tarefa_vincula_projeto_e_exibe_mensagem(self):
        response = self.client.post(
            reverse('core:tarefa_nova'),
            {
                'projeto': self.projeto.pk,
                'titulo': 'Nova tarefa',
                'descricao': 'Descrição',
                'responsavel': '',
                'prioridade': Tarefa.Prioridade.ALTA,
                'status': Tarefa.Status.EM_ANDAMENTO,
                'prazo': '',
            },
            follow=True,
        )

        tarefa_criada = Tarefa.objects.get(titulo='Nova tarefa')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('core:projeto_detalhe', args=[self.projeto.pk]),
        )
        self.assertEqual(tarefa_criada.projeto, self.projeto)
        self.assertContains(response, 'Tarefa criada com sucesso!')

    def test_cadastro_de_tarefa_sem_campos_obrigatorios_nao_salva(self):
        response = self.client.post(
            reverse('core:tarefa_nova'),
            {'projeto': '', 'titulo': ''},
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('projeto', response.context['form'].errors)
        self.assertIn('titulo', response.context['form'].errors)
        self.assertEqual(Tarefa.objects.count(), 1)

    def test_edicao_de_tarefa_atualiza_projeto_e_exibe_mensagem(self):
        response = self.client.post(
            reverse('core:tarefa_editar', args=[self.tarefa.pk]),
            {
                'projeto': self.outro_projeto.pk,
                'titulo': 'Tarefa editada',
                'descricao': 'Descrição atualizada',
                'responsavel': '',
                'prioridade': Tarefa.Prioridade.BAIXA,
                'status': Tarefa.Status.CONCLUIDA,
                'prazo': '',
            },
            follow=True,
        )

        self.tarefa.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('core:projeto_detalhe', args=[self.outro_projeto.pk]),
        )
        self.assertEqual(self.tarefa.projeto, self.outro_projeto)
        self.assertEqual(self.tarefa.status, Tarefa.Status.CONCLUIDA)
        self.assertContains(response, 'Tarefa atualizada com sucesso!')

    def test_exclusao_de_tarefa_exige_post_e_exibe_mensagem(self):
        url = reverse('core:tarefa_excluir', args=[self.tarefa.pk])
        confirmation = self.client.get(url)

        self.assertEqual(confirmation.status_code, 200)
        self.assertContains(confirmation, self.projeto.nome)
        self.assertTrue(Tarefa.objects.filter(pk=self.tarefa.pk).exists())

        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.redirect_chain[0][0],
            reverse('core:projeto_detalhe', args=[self.projeto.pk]),
        )
        self.assertFalse(Tarefa.objects.filter(pk=self.tarefa.pk).exists())
        self.assertContains(response, 'Tarefa excluída com sucesso!')


class DashboardTests(TestCase):
    def test_dashboard_indicadores_listas_links_e_estados_vazios(self):
        projeto = Projeto.objects.create(nome='Projeto do dashboard')
        pendente = Tarefa.objects.create(
            projeto=projeto,
            titulo='Tarefa pendente',
            status=Tarefa.Status.A_FAZER,
        )
        Tarefa.objects.create(
            projeto=projeto,
            titulo='Tarefa em andamento',
            status=Tarefa.Status.EM_ANDAMENTO,
        )
        Tarefa.objects.create(
            projeto=projeto,
            titulo='Tarefa concluída',
            status=Tarefa.Status.CONCLUIDA,
        )

        response = self.client.get(reverse('core:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_projetos'], 1)
        self.assertEqual(response.context['total_tarefas'], 3)
        self.assertEqual(response.context['tarefas_a_fazer'], 1)
        self.assertEqual(response.context['tarefas_em_andamento'], 1)
        self.assertEqual(response.context['tarefas_concluidas'], 1)
        self.assertContains(response, reverse('core:tarefa_editar', args=[pendente.pk]))
        self.assertContains(response, reverse('core:projeto_detalhe', args=[projeto.pk]))

    def test_dashboard_exibe_estados_vazios(self):
        response = self.client.get(reverse('core:dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ainda não há projetos cadastrados.')
        self.assertContains(response, 'Não há tarefas pendentes ou em andamento.')
        self.assertContains(response, 'Ainda não há atualizações de tarefas.')
