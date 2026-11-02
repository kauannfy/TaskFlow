# TASKFLOW — SISTEMA DE GESTÃO DE PROJETOS E TAREFAS

## 1. Apresentação do sistema

O **TaskFlow** é um sistema web desenvolvido com a finalidade de facilitar a organização, o gerenciamento e o acompanhamento de projetos e tarefas. A aplicação permitirá que os usuários cadastrem projetos, distribuam atividades, definam responsáveis e prioridades e acompanhem o andamento de cada tarefa.

A proposta é reunir, em um único ambiente, as principais informações necessárias para o gerenciamento de atividades, proporcionando uma visualização mais clara daquilo que precisa ser realizado, do que está em andamento e do que já foi concluído.

O sistema será desenvolvido utilizando tecnologias de desenvolvimento web, tendo o Django como framework para o backend e HTML, CSS e JavaScript para a construção das interfaces. Sua estrutura será organizada para permitir o cadastro, a consulta, a edição e a exclusão dos dados relacionados aos projetos e às tarefas.

## 2. Problema identificado

A organização de projetos e atividades pode se tornar complicada quando as informações ficam distribuídas entre diferentes documentos, anotações, mensagens ou ferramentas. Essa situação pode dificultar o acompanhamento das tarefas, a identificação dos responsáveis e a visualização do progresso de um projeto.

Além disso, a falta de organização pode provocar esquecimentos, atrasos, dificuldades na divisão das atividades e pouca clareza sobre quais tarefas ainda precisam ser realizadas.

Diante desse cenário, surge a necessidade de uma ferramenta que centralize essas informações e permita acompanhar as atividades de maneira simples e organizada.

O TaskFlow busca solucionar esse problema oferecendo um ambiente digital no qual os projetos e suas respectivas tarefas possam ser cadastrados, organizados e acompanhados em um único sistema.

## 3. Justificativa

O desenvolvimento do TaskFlow justifica-se pela importância de uma boa organização para a execução de projetos e atividades. Ter acesso às informações de maneira centralizada facilita o planejamento, melhora o acompanhamento das tarefas e contribui para uma distribuição mais eficiente das responsabilidades.

A utilização de um sistema web também proporciona maior praticidade, pois permite consultar e gerenciar as informações por meio de uma interface acessível em navegadores.

Além de atender a uma necessidade de organização, o desenvolvimento do projeto possibilita aplicar conhecimentos de programação, desenvolvimento web, modelagem de dados, integração entre frontend e backend e trabalho colaborativo utilizando ferramentas de versionamento.

## 4. Objetivos

### 4.1. Objetivo geral

Desenvolver um sistema web para gerenciamento de projetos e tarefas, permitindo cadastrar, organizar, visualizar e acompanhar atividades de maneira simples e centralizada.

### 4.2. Objetivos específicos

- Permitir o cadastro e o gerenciamento de projetos.
- Possibilitar a criação de tarefas vinculadas a projetos.
- Permitir a definição de responsáveis pelas tarefas.
- Possibilitar a classificação das tarefas de acordo com suas prioridades.
- Permitir a atualização e o acompanhamento do status das tarefas.
- Facilitar a visualização dos projetos e das atividades relacionadas.
- Disponibilizar funcionalidades para edição e exclusão de projetos e tarefas.
- Apresentar as informações por meio de interfaces organizadas e intuitivas.

## 5. Público-alvo

O TaskFlow é destinado a pessoas que precisam organizar projetos e acompanhar atividades de maneira prática, especialmente:

- Estudantes que desenvolvem trabalhos individuais ou em grupo.
- Pequenas equipes que precisam dividir e acompanhar tarefas.
- Pessoas que organizam projetos pessoais e atividades do cotidiano.
- Grupos que necessitam visualizar o andamento de diferentes atividades.

O sistema busca atender principalmente usuários que precisam de uma ferramenta simples para organizar suas demandas, sem depender de processos complexos de gerenciamento.

## 6. Funcionamento geral do sistema

O funcionamento do TaskFlow será baseado na organização de projetos e tarefas relacionadas a eles.

Inicialmente, o usuário poderá acessar o sistema e visualizar o Dashboard, que funcionará como um painel de acompanhamento das informações principais. Nele serão apresentados indicadores e informações resumidas sobre os projetos e as tarefas cadastradas.

A partir da navegação principal, será possível acessar a área de projetos, na qual o usuário poderá cadastrar novos projetos, visualizar os existentes, editar suas informações ou excluí-los.

Cada projeto poderá possuir diversas tarefas vinculadas. Na área de tarefas, o usuário poderá cadastrar atividades, informar seus títulos e descrições, definir responsáveis, estabelecer prioridades e acompanhar seus respectivos status.

Dessa forma, as tarefas estarão relacionadas aos projetos correspondentes, permitindo uma organização mais clara das atividades e facilitando o acompanhamento do desenvolvimento de cada projeto.

O sistema também contará com funcionalidades de edição e exclusão, permitindo manter as informações atualizadas de acordo com as necessidades dos usuários.

## 7. Principais funcionalidades

### 7.1. Cadastro e gerenciamento de projetos

Permitir a criação de projetos, o preenchimento de suas informações principais, a consulta dos projetos cadastrados, a edição de dados e a exclusão de registros.

### 7.2. Cadastro de tarefas vinculadas aos projetos

Possibilitar a criação de tarefas relacionadas a projetos existentes, permitindo organizar as atividades de acordo com o projeto ao qual pertencem.

### 7.3. Definição de responsáveis

Permitir informar quem será responsável pela realização de cada tarefa, facilitando a identificação das pessoas envolvidas nas atividades.

### 7.4. Definição de prioridades

Possibilitar a classificação das tarefas conforme seu nível de prioridade, ajudando os usuários a identificar quais atividades precisam de maior atenção.

### 7.5. Acompanhamento do status das tarefas

Permitir acompanhar a situação de cada tarefa por meio de estados que representem seu andamento, facilitando a identificação das atividades pendentes, em execução ou concluídas.

### 7.6. Visualização de projetos e atividades

Disponibilizar telas organizadas para consultar os projetos cadastrados e visualizar as tarefas relacionadas a cada um deles.

### 7.7. Edição e exclusão de registros

Permitir modificar informações de projetos e tarefas já cadastrados, assim como excluir registros quando necessário, mantendo a organização dos dados.

### 7.8. Dashboard

Apresentar um painel inicial com informações resumidas sobre os projetos e as tarefas, oferecendo uma visão geral das atividades cadastradas e facilitando o acompanhamento do sistema.

## 8. Tecnologias previstas

Para o desenvolvimento do TaskFlow, serão utilizadas as seguintes tecnologias:

- **Python:** linguagem de programação utilizada no desenvolvimento do backend.
- **Django:** framework responsável pela estrutura do sistema, gerenciamento de dados e processamento das funcionalidades.
- **HTML:** utilizado para estruturar as páginas da aplicação.
- **CSS:** responsável pela aparência, organização e estilização das interfaces.
- **JavaScript:** utilizado para implementar comportamentos e interações nas páginas.
- **SQLite:** banco de dados utilizado inicialmente para armazenar as informações dos projetos e das tarefas.
- **Git e GitHub:** ferramentas utilizadas para versionamento do código, armazenamento do projeto e colaboração entre os integrantes.

## 9. Resultados esperados

Com o desenvolvimento do TaskFlow, espera-se disponibilizar uma aplicação web funcional capaz de centralizar o gerenciamento de projetos e tarefas, tornando a organização das atividades mais simples e eficiente.

Espera-se que os usuários consigam cadastrar projetos, adicionar tarefas, definir responsáveis e prioridades e acompanhar o andamento das atividades por meio de uma interface intuitiva.

Além disso, o projeto deverá demonstrar a aplicação prática dos conhecimentos adquiridos durante o curso Técnico Integrado em Informática, envolvendo desenvolvimento frontend e backend, integração com banco de dados, organização de código e utilização de ferramentas de versionamento.

## 10. Considerações finais

O TaskFlow propõe uma solução simples para uma necessidade comum em diferentes contextos: organizar projetos e acompanhar suas atividades. Ao reunir informações sobre projetos, tarefas, responsáveis, prioridades e status em um único ambiente, o sistema pretende facilitar o planejamento e o acompanhamento das demandas.

O desenvolvimento da aplicação também representa uma oportunidade de aplicar conhecimentos técnicos na construção de um sistema web completo, desde o planejamento e a documentação até a implementação e os testes das funcionalidades.

Dessa maneira, o TaskFlow busca unir praticidade, organização e aprendizado por meio de uma ferramenta voltada ao gerenciamento de projetos e tarefas.