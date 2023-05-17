<br id="topo">

<p align="center"> <img width="200px" height="200px" src="Documenta%C3%A7%C3%A3o/photo.jpg"/> </p>

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

## Como rodar a aplicação
1. Pré-requisitos git, python3, pip3, tkinter
2. Clone o repositório `git clone`
3. Baixe o módulo virtualenv com `pip3 install virtualenv`
4. Crie um novo ambiente virtual, caso ainda não exista, com `virtualenv .venv`
5. Acessar o ambiente de execução virtual com `source .venv/bin/activate`
6. Instalar as dependências com `pip install -r requirements.txt`
7. Executar a aplicação chamando `python main.py`
 
## Objetivo

<p align="justify"> A instituição de ensino <strong> PBLTeX</strong></strong>, especializada em cursos práticos de ensino aplicando PBL (Problem Based Learning) desenvolveu uma dinâmica de <strong> Avaliação Democratizada</strong> baseada na técnica de <strong> Avaliação 360º</strong>.
A instituição vem experimentando algumas soluções de mercado e em uma análise <i>Make or Buy</i> feita recentemente, optou pelo <i>"make"</i>, ou seja, construir uma solução que viabilize a aplicação dessa dinâmina. </p>
<p align="justify"> O desafio proposto ao grupo é apoiar a <strong>PBLTeX</strong> a levantar, especificar e desenvolver uma solução computacional que viabilize a aplicação dessa técnica.</p>


<span id="Cronograma"></span>

## Cronograma

| Sprint | Link                  | Início     | Entrega    | Status     |
|--------|-----------------------|------------|------------|------------|
| --     | Kick-off              | 13/02/2023 | 03/03/2023 | ✔          |
| 01     | [Sprint 01](#sprint1) | 13/03/2023 | 02/04/2023 | ✔   |
| 02     | [Sprint 02](#sprint2) | 03/04/2023 | 23/04/2023 | ✔            |
| 03     | [Sprint 03](#sprint3) | 24/04/2023 | 14/05/2023 | Em andamento          |
| 04     | [Sprint 04](#sprint4) | 15/05/2023 | 04/06/2023 | -          |
| --     | Feira de Soluções     | 13/06/2023 | 14/06/2023 | -          |

<span id="Requisitos"></span>

## Requisitos

### Requisitos Funcionais
* Possuir um controle de usuários mínimo
* Possuir controle de perfis (administrador e integrantes)
* Possuir controle de Turmas e Times
* Possuir controle de sprints
* Deve possibilitar a realização, por um determinado integrante do Time, da avaliação 
dos demais integrantes, incluindo a sí próprio, de forma individualizada.
*  Deve prover quatro ou mais Dashboards de acompanhamento (operacional e 
gerencial)</p>

### Requisitos Não Funcionais
* Linguagem de programação Python;
* Uso de base de dados simples, como Text, CSV e ZODB;
* Uso de sistema de controle de versão de código (Git)
* Documentações</p>


<span id="Fluxograma"></span>

<details>
 <summary>

 ## Fluxograma 
 </summary>
 <img src="Documenta%C3%A7%C3%A3o/Fluxograma_app360.png" width=750>

 <span id="Diagrama"></span>

</details>

<details>
 <summary>

 ## Diagrama BPMN

 </summary>

 <img src="Documenta%C3%A7%C3%A3o/Diagrama_BPMN.png" width=750>


 <span id="Wireframe"></span>
</details>


## Esboço das telas

<details>
 <summary> Todas as telas </summary>

  <img src="Documenta%C3%A7%C3%A3o/sketchs/todas.png" width=750>

</details>

<details>
 <summary> Seleção </summary>
  
  <img src="Documenta%C3%A7%C3%A3o/sketchs/selecao.png" width=750>

</details>

<details>

 <summary> login Usuário </summary>

  <img src="Documenta%C3%A7%C3%A3o/sketchs/login_usuario.png" width=750>

</details>

<details>
 <summary> Avaliação </summary>

  <img src="Documenta%C3%A7%C3%A3o/sketchs/avaliacao.png" width=750>

</details>

<details>
 <summary> Fim da avaliação </summary>

  <img src="Documenta%C3%A7%C3%A3o/sketchs/fim_avaliacao.png" width=750> 

</details>

<details>
 <summary> Mensagem finalização </summary>
 
 <img src="Documenta%C3%A7%C3%A3o/sketchs/msg_finalizacao.png" width=750>

</details>

<details>
 <summary> Login Administrador </summary>

 <img src="Documenta%C3%A7%C3%A3o/sketchs/login_adm.png" width=750> 

</details>

<details>
 <summary> Dashboard 1 </summary>

 <img src="Documenta%C3%A7%C3%A3o/sketchs/dashboard_1.png" width=750>

</details>

<details>
 <summary> Dashboard 2 </summary>

<img src="Documenta%C3%A7%C3%A3o/sketchs/dashboard_2.png" width=750> 

</details>

<span id="backlog"></span>

## Product Backlog
| ID | User Stories                                                                                                           | Backlog                                                                      | Sprint                                                    | Prioridade |
|----|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------|------------|
|1   | Armazenar as infomações de desenvolvimento e administrar a evolução de cada integrante da equipe.                      | Criação/Organização do GitHub                                                |[#01](https://github.com/orgs/flapjackdevteam/projects/7) | Essencial  | 
|2   | Definição do fluxo de interação do usuário.                                                                            | Fluxograma                                                                   |[#01](https://github.com/orgs/flapjackdevteam/projects/7) | Importante |
|3   | Poder apresentar uma ideia base de como seria a experiência do usuário e apresentação do software.                     | Esboço de tela                                                               |[#01](https://github.com/orgs/flapjackdevteam/projects/7) | Importante |
|4   | Demonstar a interface inicial e funcionalidade do login do administrador e usuário                                     | Protótipo de tela de login do administrador e usuário                        |[#01](https://github.com/orgs/flapjackdevteam/projects/7) | Desejável  |
|5   | Ter uma possível previsão da entrega de cada Sprint futura.                                                            | Planejamento das outras Sprints (2, 3 e 4)                                   |[#01](https://github.com/orgs/flapjackdevteam/projects/7) | Essencial  |
|6   | Separar as funcionalidades atribuidas ao administrador dos usuários.                                                   | Sistema de gerenciamento, cadastro e controle do Administrador no aplicativo |[#02](https://github.com/orgs/flapjackdevteam/projects/9) | Importante |
|7   | Planejar, visualizar e organizar as perguntas utilizadas na avaliação.                                                 | Tela de avaliação 360º do usuário.                                           |[#02](https://github.com/orgs/flapjackdevteam/projects/9) | Essencial  |
|8   | Parte funcional da avaliação onde irá gerar os dados com base nas perguntas para ralização dos Dashboards.             | Definir e implementar o sistema de avaliação 360º                            |[#02](https://github.com/orgs/flapjackdevteam/projects/9) | Importante |
|9   | Criar arquivo JSON contendo informações de login de usuário comum e administrador para implementar controle de acesso. | Definir e implementar base de dados contendo usuários e administrador        |[#02](https://github.com/orgs/flapjackdevteam/projects/9) | Importante |
|10  | Detalhar dados e informações dos Dashboards.                                                                           | Definir os Dashboards                                                        |[#03](https://github.com/orgs/flapjackdevteam/projects/10)| Essencial  |
|11  | Visualizar as respostas consolidadas referente ao Time e seus membros.                                                 | Dashboard do Time                                                            |[#03](https://github.com/orgs/flapjackdevteam/projects/10)| Importante |
|12  | Visualizar as respostas consolidadas para cada membro individualmente.                                                 | Dashboard individual para cada usuário                                       |[#03](https://github.com/orgs/flapjackdevteam/projects/10)| Importante |
|13  | Demonstrar como foi o desempenho da equipe durante a Sprint.                                                           | Dashboard da Sprint                                                          |[#03](https://github.com/orgs/flapjackdevteam/projects/10)| Importante |
|14  | Garantir que o código esteja funcionando conforme esperado.                                                            | Revisão de código                                                            |[#04](https://github.com/orgs/flapjackdevteam/projects/11)| Essencial  |
|15  | Garantir que todos requisitos funcionais estão aderentes as exigências do cliente.                                     | Controle de qualidade                                                        |[#04](https://github.com/orgs/flapjackdevteam/projects/11)| Essencial  |
|16  | Executar e analisar o código linha por linha para identificar algum erro ou problema.                                  | Debuggin                                                                     |[#04](https://github.com/orgs/flapjackdevteam/projects/11)| Essencial  |
|17  | Garantir a implementação correta e funcional do software de acordo com as especificações projeto.                      | Refinamento do software                                                      |[#04](https://github.com/orgs/flapjackdevteam/projects/11)| Essencial  |


<span id="Tecnologias"></span>

## Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [PySimpleGui](https://www.pysimplegui.org/en/latest/)
* [Git/Github (Controle de versão)](https://github.com/)
* [Figma](https://www.figma.com/)
* [VsCode](https://code.visualstudio.com/)
* [Visio](https://www.microsoft.com/pt-br/microsoft-365/visio/flowchart-software)

<span id="Links"></span>

## Links Importantes

[Links Importantes de ferramentas, tutoriais e ideias para o projeto API](Documenta%C3%A7%C3%A3o/Links%20Importantes%20de%20ferramentas%2C%20tutoriais%20e%20ideias%20para%20o%20projeto%20API.md)

<span id="Equipe"></span>

## Equipe

| Nome                                      | Função        |LinkedIn|GitHub|
|-------------------------------------------|---------------|-------- |-------- |
| **Gleialison dos Santos**                 | Product Owner |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/gleialison-rezende-835453b0)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/Gleialison)|
| **Rodrigo dos Santos**                    | Scrum Master  |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/rodrigo-dos-santos-pinto-da-cunha-a299a6169/)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/rodrigo-spcunha)|
| **Aguinaldo Cardoso de Macedo Júnior**    | Dev     |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&color=7f7f7f" />](#)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/aguinaldojunior31)|
| **David Astolpho Mendes**                 | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&color=7f7f7f" />](#)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/David5Mende5)|
| **Fátima Leise de Oliveira**              | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/f%C3%A1tima-leise-oliveira-37724b76/)| [<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/fatimaleise)|
| **Heitor Cardoso Nogueira**               | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&color=7f7f7f" />](#)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/HeitorCarNog)|
| **Júlio César Barbosa da Rosa Rodrigues** | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](http://www.linkedin.com/in/jcbarbosarosa)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/jcbarbosarosa)|
| **Michel Momose Marques**                 | Dev      |[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white&color=7f7f7f" />](#)|[<img src="https://camo.githubusercontent.com/fbc3df79ffe1a99e482b154b29262ecbb10d6ee4ed22faa82683aa653d72c4e1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d3130303030303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d7768697465" />](https://github.com/Michel-Momose)|
