import PySimpleGUI as sg
import json

usuarios_nao_avaliados = []
usuario_atual = None
perguntas = ["Engajamento e Pró-atividade",
             "Auto-gestão das Atividades",
             "Comunicação e Trabalho em Equipe",
             "Conhecimento e Aplicabilidade Técnica",
             "Entrega de Resultados com Valor Agregado"]

# Define a função para atualizar o usuário atual e a lista de usuários não avaliados
def atualizar_usuario_e_usuarios_nao_avaliados(usuario):
    global usuario_atual, usuarios_nao_avaliados
    usuario_atual = usuario
    usuarios_nao_avaliados = [u for u in usuarios_nao_avaliados if u['matricula'] != usuario['matricula']]

# Define a função para obter o próximo usuário a ser avaliado
def obter_proximo_usuario():
    for usuario in usuarios_nao_avaliados:
        if usuario['matricula'] != usuario_atual['matricula']:
            return usuario
    return None

def layout_questionario(layout):
    layout.append([sg.HSeparator(pad=(0,0))])

    layout.append([
        sg.Text(' ', font=('Arial', 12), size=(41, 1)),
        sg.Text('1', font=('Arial', 12), size=(3, 1)),
        sg.Text('2', font=('Arial', 12), size=(3, 1)),
        sg.Text('3', font=('Arial', 12), size=(3, 1)),
        sg.Text('4', font=('Arial', 12), size=(3, 1)),
        sg.Text('5', font=('Arial', 12), size=(3, 1)),
        ])
    
    layout.append([sg.HSeparator(pad=(0,0))])
    
    for i in range(0, len(perguntas)):
        layout.append([
            sg.Text(perguntas[i], font=('Arial', 12), size=(40, 1)),
            sg.Radio('', i, default=False, size=(1, 1), key=f"pergunta-{i}-opcao-1"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"pergunta-{i}-opcao-2"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"pergunta-{i}-opcao-3"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"pergunta-{i}-opcao-4"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"pergunta-{i}-opcao-5")
        ])

    layout.append([sg.HSeparator(),sg.Text("0-Ruim, 1-Regular, 2-Bom, 3-Excelente")])

def layout_avaliacao(nome):
    # Define o layout da janela de avaliação
    layout = []
    layout = [
    [sg.Text('Você está avaliando o usuário ' + nome,
            font=('Arial', 18), justification='center', background_color='white', size=(40, 0),
            relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
    [sg.Text('Responda ao questionário abaixo:', font=('Arial', 14), size=(40, 1))]
    ]

    button_layout = [[sg.Button("Individual", key="individual", disabled=True, size=(10,2), button_color=('white', 'gray'))],
                    [sg.Button("Equipe", key="equipe", disabled=True, size=(10,2), button_color=('white', 'gray'))],
                    [sg.Button("Turma", key="turma", disabled=True, size=(10,2), button_color=('white', 'gray'))],
                    [sg.HSeparator()],
                    [sg.Button("Limpar", key="limpar", size=(10,2))],
                    [sg.Button("Sair", key="sair", size=(10,2))]]

    # Insere o layout das perguntas
    questionario = []
    layout_questionario(questionario)
    #layout.append([sg.Frame('Avalie ' + nome, questionario)])

    layout.append([sg.Column(button_layout),
                   sg.VSeparator(),
                   sg.Column(questionario)
    ])

    # Adicionar o botão de enviar para a janela de avaliação
    layout.append(
    [sg.Button('Próximo', key='proximo', size=(20, 2),
                button_color=('white', 'black'),
                font=('Helvetica', 20),
                disabled=False)
                ])

    return layout

# Função para obter as opções selecionadas
def opcoes_selecionadas(values):
    respostas = {}
    for i in range(0, len(perguntas)):
        for j in range(1, 5):
            if values[f"pergunta-{i}-opcao-{j}"]:
                #print(f"pergunta-{i}-opcao-{j}")
                respostas.update({f"p{i}": j})
    return respostas

def tela_avaliacao(usuario):
    global usuarios_nao_avaliados, usuario_atual
    print("Abrindo a tela de avaliação")

    # Carrega um tema pré definido do PySimpleGui
    sg.theme('DefaultNoMoreNagging')

    # Carrega o conteúdo do arquivo data.json em um dicionário Python
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Carrega o arquivo avaliações.json
    avaliacoes = {}
    with open('avaliacoes.json', 'r', encoding='utf-8') as f:
        avaliacoes = json.load(f)

    # Armazena a lista de usuários não avaliados
    usuarios_nao_avaliados = [usuario for usuario in data['usuarios'] if usuario['matricula'] != 'admin']

    atualizar_usuario_e_usuarios_nao_avaliados(usuario)
    # Cria a janela de avaliação
    respostas = []  # Criar uma lista para armazenar as respostas

    avaliacao_layout = layout_avaliacao(usuario["nome"])

    # Cria a janela de avaliação
    avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout, finalize=True,
                            resizable=True, element_padding=(20, 20))

    avaliacao_janela['individual'].update(disabled=False, button_color=('white', 'green'))

    # Definir o tamanho mínimo da janela
    avaliacao_janela.set_min_size((800, 600))

    avaliacao_janela_anterior = avaliacao_janela

    avaliacao = {"sprint": "", "tipo": "individual", f"matricula": f"{usuario['matricula']}", "respostas": {}}
    print(avaliacao)    

    # Loop de eventos da janela de avaliação
    while True:
        event, values = avaliacao_janela.read()

        if event == sg.WIN_CLOSED:
            break

        # Limpa as opções elecionadas
        elif event == 'limpar':
            for i in range(0, len(perguntas)):
                for j in range(1, 6):
                    if values[f"pergunta-{i}-opcao-{j}"]:
                        avaliacao_janela[f'pergunta-{i}-opcao-{j}'].Update(False)
            continue

        elif event == 'proximo':
            # Obtém as opções selecionadas
            respostas = opcoes_selecionadas(values)
            print(opcoes_selecionadas(values))
                    
            # Verifica se aquantidade de respostas é menor que a quantidade de perguntas
            if len(respostas) < len(perguntas):
                sg.popup("Preencha todas os tópicos antes de continuar")
                continue

            # Código para armazenar a avaliação em uma estrutura temporária
            avaliacao.update({"respostas": respostas})
            print(avaliacao)

            avaliacoes.update({"1460282313028": ["avaliacao"].append(avaliacao)})
            print(avaliacoes)

            # Atualiza o usuário atual e a lista de usuários não avaliados
            atualizar_usuario_e_usuarios_nao_avaliados(usuario_atual)
            # Verifica se ainda há usuários não avaliados
            if not usuarios_nao_avaliados:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação')
                break

            # Obtém o próximo usuário a ser avaliado
            proximo_usuario = obter_proximo_usuario()
            if proximo_usuario:
                avaliacao_layout = layout_avaliacao(proximo_usuario["nome"])

                # Cria a janela de avaliação
                avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout,
                                            finalize=True, resizable=True,
                                            element_padding=(20, 20))
                
                avaliacao_janela['equipe'].update(disabled=False, button_color=('white', 'green'))

                # Definir o tamanho mínimo da janela
                avaliacao_janela.set_min_size((800, 600))

                # Atualiza o usuário atual e a janela principal
                usuario_atual = proximo_usuario
                avaliacao_janela_anterior.close()
                avaliacao_janela_anterior = avaliacao_janela

            else:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação', keep_on_top=True)
                break
        elif event == 'sair':
            avaliacao_janela.close()
            break

tela_avaliacao({'nome': 'Rodrigo Santos', 'matricula': '1460282313028'})