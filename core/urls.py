from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),

    path('projetos/', views.ProjetoListView.as_view(), name='projeto_lista'),
    path('projetos/novo/', views.ProjetoCreateView.as_view(), name='projeto_novo'),
    path('projetos/<int:pk>/', views.ProjetoDetailView.as_view(), name='projeto_detalhe'),
    path('projetos/<int:pk>/editar/', views.ProjetoUpdateView.as_view(), name='projeto_editar'),
    path('projetos/<int:pk>/excluir/', views.ProjetoDeleteView.as_view(), name='projeto_excluir'),

    path('tarefas/', views.TarefaListView.as_view(), name='tarefa_lista'),
    path('tarefas/nova/', views.TarefaCreateView.as_view(), name='tarefa_nova'),
    path('tarefas/<int:pk>/editar/', views.TarefaUpdateView.as_view(), name='tarefa_editar'),
    path('tarefas/<int:pk>/excluir/', views.TarefaDeleteView.as_view(), name='tarefa_excluir'),
]