# TASKFLOW — ESPECIFICAÇÃO DE REQUISITOS

## 1. Introdução

Este documento apresenta os requisitos funcionais e não funcionais do TaskFlow, uma aplicação web de uso individual para gerenciamento de projetos e tarefas.

O objetivo desta documentação é descrever as funcionalidades disponíveis na aplicação e as características de qualidade consideradas no seu desenvolvimento.

Os requisitos aqui definidos registram as funcionalidades do sistema e suas características de qualidade, servindo como referência para a manutenção e evolução da aplicação.

## 2. Descrição geral do sistema

O TaskFlow é uma aplicação web de uso individual que permite organizar projetos e gerenciar as tarefas relacionadas a cada um deles.

O sistema permite cadastrar, consultar, editar e excluir projetos e tarefas, além de definir responsáveis opcionais, prioridades e status das atividades.

A aplicação conta com uma interface organizada, incluindo um Dashboard com informações resumidas e páginas específicas para o gerenciamento de projetos e tarefas.

O sistema utiliza Python e Django no backend, HTML, CSS e JavaScript no frontend, além de um banco de dados para armazenar as informações.

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

O sistema deverá permitir a exclusão de projetos cadastrados mediante confirmação. Após a confirmação, as tarefas vinculadas ao projeto serão excluídas automaticamente junto com ele.

### RF05 — Cadastrar tarefas

O sistema deverá permitir o cadastro de novas tarefas, com informações como título, descrição, responsável opcional, prioridade e status.

### RF06 — Vincular tarefas a projetos

O sistema deverá permitir associar cada tarefa a um projeto existente, possibilitando organizar as atividades de acordo com o projeto correspondente.

### RF07 — Listar tarefas

O sistema deverá apresentar as tarefas cadastradas, permitindo visualizar suas principais informações e identificar a qual projeto pertencem.

### RF08 — Editar tarefas

O sistema deverá permitir a alteração das informações de tarefas existentes, incluindo título, descrição, responsável opcional, prioridade e demais campos disponíveis.

### RF09 — Excluir tarefas

O sistema deverá permitir a exclusão de tarefas cadastradas quando necessário.

### RF10 — Definir responsáveis pelas tarefas

O sistema deverá permitir associar opcionalmente a cada tarefa um usuário já cadastrado no Django como responsável, facilitando sua identificação. No escopo individual do TaskFlow, esse campo não representa gerenciamento de equipes, cadastro de usuários ou colaboração entre pessoas.

### RF11 — Definir prioridades das tarefas

O sistema deverá permitir classificar as tarefas com as prioridades Baixa, Média e Alta, facilitando a identificação das atividades que precisam de maior atenção.

### RF12 — Atualizar o status das tarefas

O sistema deverá permitir alterar o status das tarefas entre A fazer, Em andamento e Concluída, possibilitando acompanhar seu andamento.

### RF13 — Visualizar tarefas relacionadas a um projeto

O sistema deverá permitir consultar as tarefas vinculadas a um projeto específico, facilitando o acompanhamento das atividades relacionadas a ele.

### RF14 — Exibir Dashboard

O sistema deverá disponibilizar um painel inicial com o total de projetos, o total de tarefas e a quantidade de tarefas por status, além de apresentar projetos recentes, tarefas em aberto e atualizações recentes.

## 4. Requisitos não funcionais

Os requisitos não funcionais estabelecem características de qualidade, desempenho, organização e funcionamento que deverão ser consideradas durante o desenvolvimento do TaskFlow.

Cada requisito recebe um código de identificação iniciado por RNF, seguido de um número sequencial.

### RNF01 — Usabilidade

O sistema deverá apresentar uma interface intuitiva e organizada, permitindo que os usuários encontrem as funcionalidades e realizem as operações disponíveis sem dificuldades desnecessárias.

### RNF02 — Organização visual

As páginas deverão manter um padrão visual consistente, utilizando elementos de interface organizados e uma disposição clara das informações.

### RNF03 — Compatibilidade

Espera-se que o sistema funcione nos principais navegadores modernos, como Google Chrome, Mozilla Firefox e Microsoft Edge, respeitando suas versões atuais e recursos compatíveis.

### RNF04 — Responsividade

Espera-se que as interfaces se adaptem adequadamente a diferentes tamanhos de tela, permitindo a utilização do sistema tanto em computadores quanto em dispositivos móveis.

### RNF05 — Desempenho

Espera-se que as páginas e operações principais apresentem tempo de resposta adequado durante a utilização normal do sistema, evitando atrasos desnecessários na consulta e no gerenciamento de projetos e tarefas.

### RNF06 — Integridade dos dados

O sistema deverá manter a consistência das informações armazenadas, garantindo que os relacionamentos entre projetos e tarefas sejam respeitados durante as operações de cadastro, edição e exclusão.

### RNF07 — Manutenibilidade

O código-fonte deverá ser organizado e estruturado de maneira que facilite a identificação, correção de erros e implementação de futuras melhorias.

### RNF08 — Validação de dados

O sistema deverá validar os dados enviados pelos formulários antes de salvá-los, verificando o preenchimento dos campos obrigatórios e a consistência das informações. Quando houver dados inválidos, deverá apresentar mensagens de erro ao usuário.

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