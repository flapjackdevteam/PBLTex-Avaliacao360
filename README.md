<br id="topo">

<p align="center"> <img src="https://github.com/flapjackdevteam/PBLTex-Avaliacao360/blob/dev/Documenta%C3%A7%C3%A3o/photo.jpg"/> </p>

<h1 align="center"> FLAPJACK DevTeam</h1>


 <p align="center"> |
    <a href="#objetivo">Objetivo</a> |
    <a href="#cronograma">Cronograma</a> |
    <a href="#requisitos">Requisitos</a> |
    <a href="#fluxograma">Fluxograma</a> |
    <a href="#Diagrama">Diagrama BPMN</a> |
    <a href="#preview">Wireframe</a> | 
    <a href="#backlog">Product Backlog</a> |
    <a href="#tecnologias">Tecnologias utilizadas</a> |
    <a href="#links">Links importantes</a> | 
    <a href="#equipe">Equipe</a> |
    
</p>
   
<span id="Objetivo"></span>

## Objetivo

<p align="justify"> A instituição de ensino <strong> PBLTeX</strong></strong>, especializada em cursos práticos de ensino aplicando PBL (Problem Based Learning) desenvolveu uma dinâmica de <strong> Avaliação Democratizada</strong> baseada na técnica de <strong> Avaliação 360º</strong>.
A instituição vem experimentando algumas soluções de mercado e em uma análise <i>Make or Buy</i> feita recentemente, optou pelo <i>"make"</i>, ou seja, construir uma solução que viabilize a aplicação dessa dinâmina. </p>
<p align="justify"> O desafio proposto ao grupo é apoiar a <strong>PBLTeX</strong> a levantar, especificar e desenvolver uma solução computacional que viabilize a aplicação dessa técnica.</p>


<span id="Cronograma"></span>

## Cronograma

| Sprint | Link                  | Início     | Entrega    |   Status     |
|--------|-----------------------|------------|------------|:-------------:
| --     | Kick-off              | 13/02/2023 | 03/03/2023 |      ✔       |
| 01     | [Sprint 01](#sprint1) | 13/03/2023 | 02/04/2023 | em andamento |
| 02     | [Sprint 02](#sprint2) | 03/04/2023 | 23/04/2023 |      -       |
| 03     | [Sprint 03](#sprint3) | 24/04/2023 | 14/05/2023 |      -       |
| 04     | [Sprint 04](#sprint4) | 15/05/2023 | 04/06/2023 |      -       |
| --     | Feira de Soluções     | 13/06/2023 | 14/06/2023 |      -       |

<span id="Requisitos"></span>

## Requisitos

### Requisitos Funcionais
<p align="justify"> * Possuir um controle de usuários mínimo
<p align="justify">* Possuir controle de perfis (administrador e integrantes)
<p align="justify">* Possuir controle de Turmas e Times
<p align="justify">* Possuir controle de sprints
<p align="justify">* Deve possibilitar a realização, por um determinado integrante do Time, da avaliação 
dos demais integrantes, incluindo a sí próprio, de forma individualizada.
<p align="justify">*  Deve prover quatro ou mais Dashboards de acompanhamento (operacional e 
gerencial)</p>

### Requisitos Não Funcionais
<p align="justify">* Linguagem de programação Python;
<p align="justify">* Uso de base de dados simples, como Text, CSV e ZODB;
<p align="justify">* Uso de sistema de controle de versão de código (Git)
<p align="justify">* Documentações</p>

<span id="Fluxograma"></span>

## Fluxograma

![Fluxograma](https://github.com/flapjackdevteam/PBLTex-Avaliacao360/blob/dev/Documenta%C3%A7%C3%A3o/Fluxograma_app360.png)

<span id="Diagrama"></span>

## Diagrama BPMN

![Diagrama](https://github.com/flapjackdevteam/PBLTex-Avaliacao360/blob/dev/Documenta%C3%A7%C3%A3o/Diagrama_BPMN.png)


<span id="Wireframe"></span>

## Wireframe

<span id="backlog"></span>

## Product Backlog

<span id="sprint1"></span>

> ## Sprint 1

| INSTRUÇÃO                                                        | FINALIDADE                                                                                            | O QUE FAZER                                                                                                                                                                                         |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| Criação/Organização do GitHubCriação                             | Armazenar as infomações de desenvolvimento e administrar a evolução de cada integrante da equipe      | Ter um read.me estruturado com todas as informações                                                                                                                                                 |  
| Definir o MVP                                                    | Separar e definir os requisitos funcionais mínimos necessários para entrega de um programa funcional. | Desenvolver um software que possibilite o administrador cadastar os integrantes de um time e obter o resultado  gerenciais  através dos dashboads gerados e os usuários realizar as avaliações 360. |
| Fluxograma                                                       | Definição do passo a passo em cada fase do projeto                                                    | Pensar e montar o fluxo de interação do usuário no programa.                                                                                                                                        |
| Prototipo de tela de login do administrador e usuário            | Demonstar a interface inicial e funcionalidade do login do administrador e usuário                    | Começar a escrever o código base utilizando o SimpleGui                                                                                                                                             |
| Dividir o o administrador do usuários que irá fazer a avaliação  | Para que o administrador consiga cadastrar os usuários e os mesmos poderem realizar as avaliações     | Idealizar e desenvolver com a equipe o passo a passo                                                                                                                                                |
| Planejamento das outras Sprints (2, 3 e 4)                       | Ter uma possível previsão da entrega de cada Sprint futura                                            | Idealizar e desenvolver com a equipe o passo a passo                                                                                                                                                |

<span id="sprint2"></span>
> ### Sprint 02

| INSTRUÇÃO                                                                    | FINALIDADE                                                                                                              | O QUE FAZER  |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------|
 | Sistema de gerenciamento, cadastro e controle do Administrador no aplicativo | Separar as funcionalidades atribuidas ao administrador dos usuários.                                                    | ---          |
| Tela de avaliação 360 do usuário.                                            | Planejar, visualizar e organizar as perguntas utilizadas na avaliação                                                   | ---          |
 | Definir e implementar o sistema de avaliação 360º                            | Parte funcional da avaliação onde irá gerar os dados com base nas perguntas para ralização dos Dashboards               | ---          |
 | Definir e implementar base de dados contendo usuários e administrador        | Criar arquivo .json contendo informações de login de usuário comum e administrador para implementar controle de acesso. | ---          |

<span id="sprint3"></span>
> ### Sprint 03

<span id="sprint4"></span>
> ### Sprint 04

<span id="Tecnologias"></span>

## Tecnologias Utilizadas

<p align="justify"> * Python
<p align="justify"> * Git/Github (Controle de versão)
<p align="justify"> * Figma
<p align="justify"> * VsCode
<p align="justify"> * Microsoft Excel
<p align="justify"> * Visio

<span id="Links"></span>

## Links Importantes

Disponível em: https://github.com/flapjackdevteam/PBLTex-Avaliacao360/blob/main/Documenta%C3%A7%C3%A3o/Links%20Importantes%20de%20ferramentas%2C%20tutoriais%20e%20ideias%20para%20o%20projeto%20API.md


<span id="Equipe"></span>

## Equipe


| Nome                                      | Função        |LinkedIn|GitHub|
|-------------------------------------------|---------------|-------- |-------- |
| **Gleialison dos Santos**                 | Product Owner |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **Rodrigo dos Santos**                    | Scrum Master  |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **Aguinaldo Cardoso de Macedo Júnior**    | Dev     |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **David Astolpho Mendes**                 | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **Fátima Leise de Oliveira**              | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/f%C3%A1tima-leise-oliveira-37724b76/)| [<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/fatimaleise)|
| **Heitor Cardoso Nogueira**               | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **Júlio César Barbosa da Rosa Rodrigues** | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](http://www.linkedin.com/in/jcbarbosarosa)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/jcbarbosarosa)|
| **Lucas de Freitas Venancio**             | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|
| **Michel Momose Marques**                 | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />]()|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/Michel-Momose)|
| **Rodrigo Pereira**                       | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/mwlite/in/rodrigo-pereira-de-castro-09758853)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />]()|




