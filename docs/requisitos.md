# TASKFLOW — ESPECIFICAÇÃO DE REQUISITOS

## 1. Introdução

Este documento apresenta a especificação dos requisitos funcionais e não funcionais do TaskFlow, um sistema web destinado ao gerenciamento de projetos e tarefas.

O objetivo desta documentação é estabelecer as funcionalidades que deverão estar disponíveis na aplicação e as características de qualidade que deverão ser consideradas durante seu desenvolvimento.

Os requisitos aqui definidos servirão como referência para a implementação do sistema, orientando a construção das interfaces, a estruturação do banco de dados e o desenvolvimento das funcionalidades do backend.

## 2. Descrição geral do sistema

O TaskFlow será uma aplicação web que permitirá organizar projetos e gerenciar as tarefas relacionadas a cada um deles.

O sistema possibilitará cadastrar, consultar, editar e excluir projetos e tarefas, além de permitir a definição de responsáveis, prioridades e status das atividades.

A aplicação contará com uma interface organizada, incluindo um Dashboard para apresentar informações resumidas e páginas específicas para o gerenciamento de projetos e tarefas.

O desenvolvimento será realizado utilizando Python e Django no backend, HTML, CSS e JavaScript no frontend, além de um banco de dados para armazenar as informações.

## 3. Requisitos funcionais

Os requisitos funcionais descrevem as operações e funcionalidades que o sistema deverá oferecer aos usuários.

Cada requisito recebe um código de identificação iniciado por RF, seguido de um número sequencial.

### RF01 — Cadastrar projetos

O sistema deverá permitir o cadastro de novos projetos, possibilitando o preenchimento das informações necessárias para sua identificação e descrição.

### RF02 — Listar projetos

O sistema deverá apresentar uma listagem dos projetos cadastrados, permitindo que o usuário visualize e consulte os projetos existentes.

### RF03 — Editar projetos

O sistema deverá permitir a alteração das informações de projetos já cadastrados, mantendo os dados atualizados.

### RF04 — Excluir projetos

O sistema deverá permitir a exclusão de projetos cadastrados, respeitando os relacionamentos existentes com suas tarefas para evitar inconsistências nos dados.

### RF05 — Cadastrar tarefas

O sistema deverá permitir o cadastro de novas tarefas, com informações como título, descrição, responsável, prioridade e status.

### RF06 — Vincular tarefas a projetos

O sistema deverá permitir associar cada tarefa a um projeto existente, possibilitando organizar as atividades de acordo com o projeto correspondente.

### RF07 — Listar tarefas

O sistema deverá apresentar as tarefas cadastradas, permitindo visualizar suas principais informações e identificar a qual projeto pertencem.

### RF08 — Editar tarefas

O sistema deverá permitir a alteração das informações de tarefas existentes, incluindo título, descrição, responsável, prioridade e demais campos disponíveis.

### RF09 — Excluir tarefas

O sistema deverá permitir a exclusão de tarefas cadastradas quando necessário.

### RF10 — Definir responsáveis pelas tarefas

O sistema deverá permitir informar o responsável pela realização de cada tarefa, facilitando a identificação de quem deverá executar a atividade.

### RF11 — Definir prioridades das tarefas

O sistema deverá permitir classificar as tarefas de acordo com seus níveis de prioridade, facilitando a identificação das atividades que precisam de maior atenção.

### RF12 — Atualizar o status das tarefas

O sistema deverá permitir alterar o status das tarefas conforme seu andamento, possibilitando identificar atividades pendentes, em execução ou concluídas.

### RF13 — Visualizar tarefas relacionadas a um projeto

O sistema deverá permitir consultar as tarefas vinculadas a um projeto específico, facilitando o acompanhamento das atividades relacionadas a ele.

### RF14 — Exibir Dashboard

O sistema deverá disponibilizar um painel inicial com informações resumidas sobre os projetos e as tarefas cadastradas, apresentando indicadores e informações relevantes para o acompanhamento das atividades.

## 4. Requisitos não funcionais

Os requisitos não funcionais estabelecem características de qualidade, desempenho, organização e funcionamento que deverão ser consideradas durante o desenvolvimento do TaskFlow.

Cada requisito recebe um código de identificação iniciado por RNF, seguido de um número sequencial.

### RNF01 — Usabilidade

O sistema deverá apresentar uma interface intuitiva e organizada, permitindo que os usuários encontrem as funcionalidades e realizem as operações disponíveis sem dificuldades desnecessárias.

### RNF02 — Organização visual

As páginas deverão manter um padrão visual consistente, utilizando elementos de interface organizados e uma disposição clara das informações.

### RNF03 — Compatibilidade

O sistema deverá funcionar nos principais navegadores modernos, como Google Chrome, Mozilla Firefox e Microsoft Edge, respeitando suas versões atuais e recursos compatíveis.

### RNF04 — Responsividade

As interfaces deverão apresentar adaptação adequada a diferentes tamanhos de tela, permitindo a utilização do sistema tanto em computadores quanto em dispositivos móveis.

### RNF05 — Desempenho

As páginas e operações principais deverão apresentar tempo de resposta adequado durante a utilização normal do sistema, evitando atrasos desnecessários na consulta e no gerenciamento de projetos e tarefas.

### RNF06 — Integridade dos dados

O sistema deverá manter a consistência das informações armazenadas, garantindo que os relacionamentos entre projetos e tarefas sejam respeitados durante as operações de cadastro, edição e exclusão.

### RNF07 — Manutenibilidade

O código-fonte deverá ser organizado e estruturado de maneira que facilite a identificação, correção de erros e implementação de futuras melhorias.

### RNF08 — Validação de dados

O sistema deverá validar as informações fornecidas nos formulários, impedindo o armazenamento de dados inválidos ou o envio de campos obrigatórios sem preenchimento.

### RNF09 — Armazenamento

As informações dos projetos e das tarefas deverão ser armazenadas em banco de dados, permitindo sua recuperação e consulta posteriormente.

### RNF10 — Tecnologias e estrutura

O desenvolvimento deverá respeitar a arquitetura tecnológica definida para o projeto, utilizando Django no backend, HTML, CSS e JavaScript no frontend e uma estrutura organizada para os arquivos e componentes da aplicação.

## 5. Relação entre os requisitos e as funcionalidades

A tabela a seguir apresenta uma visão resumida da relação entre os requisitos e as principais áreas do TaskFlow.

| Área do sistema | Requisitos relacionados |
|---|---|
| Gerenciamento de projetos | RF01, RF02, RF03 e RF04 |
| Gerenciamento de tarefas | RF05, RF07, RF08 e RF09 |
| Organização das atividades | RF06, RF10, RF11 e RF12 |
| Acompanhamento dos projetos | RF13 e RF14 |
| Qualidade da interface | RNF01, RNF02, RNF03 e RNF04 |
| Qualidade técnica | RNF05, RNF06, RNF07, RNF08, RNF09 e RNF10 |

## 6. Considerações finais

A definição dos requisitos funcionais e não funcionais é uma etapa importante para orientar o desenvolvimento do TaskFlow, pois estabelece as funcionalidades esperadas e as características que deverão ser atendidas pela aplicação.

Os requisitos apresentados servirão como referência para a implementação do sistema e para a realização dos testes, permitindo verificar se as funcionalidades desenvolvidas correspondem ao que foi planejado.

Dessa forma, a documentação contribui para manter a organização do projeto, facilitar a comunicação entre os integrantes da equipe e garantir que o desenvolvimento siga os objetivos estabelecidos inicialmente.