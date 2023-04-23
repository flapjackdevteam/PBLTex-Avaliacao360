import PySimpleGUI as sg
import csv
import json

usuarios_nao_avaliados = []
usuario_atual = None

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

def tela_avaliacao(usuario):
    global usuarios_nao_avaliados, usuario_atual
    print("Abrindo a tela de avaliação")

    # Carrega um tema pré definido do PySimpleGui
    sg.theme('DefaultNoMoreNagging')

    # Carrega o conteúdo do arquivo data.json em um dicionário Python
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Armazena a lista de usuários não avaliados
    usuarios_nao_avaliados = [usuario for usuario in data['usuarios'] if usuario['matricula'] != 'admin']

    atualizar_usuario_e_usuarios_nao_avaliados(usuario)
    # Cria a janela de avaliação
    perguntas = []
    respostas = []  # Criar uma lista para armazenar as respostas
    with open('perguntas.csv', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            pergunta = {
                'pergunta': linha[0],
                'opcoes': linha[1:]
            }
            perguntas.append(pergunta)

    # Define o layout da janela de avaliação
    avaliacao_layout = [
    [sg.Text(f'Você está avaliando o usuário {usuario["nome"]}',
            font=('Arial', 18), justification='center', background_color='white', size=(30, 1),
            relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
    [sg.Text('Responda as seguintes perguntas:', font=('Arial', 18), size=(40, 1))]
    ]

    # Insere as perguntas
    for i, pergunta in enumerate(perguntas):
        avaliacao_layout.append([
            sg.Text(f'{i + 1}. {pergunta["pergunta"]}', font=('Arial', 18), size=(40, 1)),
            sg.Radio('0', f'resposta-{i}', default=False, size=(4, 1), key=f'pergunta-{i}-opcao-0'),
            sg.Radio('1', f'resposta-{i}', default=False, size=(4, 1), key=f'pergunta-{i}-opcao-1'),
            sg.Radio('2', f'resposta-{i}', default=False, size=(4, 1), key=f'pergunta-{i}-opcao-2'),
            sg.Radio('3', f'resposta-{i}', default=False, size=(4, 1), key=f'pergunta-{i}-opcao-3')
        ])

    # Adicionar o botão de enviar para a janela de avaliação
    avaliacao_layout.append(
    [sg.Button('Enviar Avaliação', size=(20, 2), button_color=('white', 'black'),
            font=('Helvetica', 20))])

    # Cria a janela de avaliação
    avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout, finalize=True,
                            resizable=True, element_padding=(20, 20))

    # Definir o tamanho mínimo da janela
    avaliacao_janela.set_min_size((800, 600))

    # Loop de eventos da janela de avaliação
    while True:
        event, values = avaliacao_janela.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == 'Enviar Avaliação':
            # Código para enviar a avaliação...
            # Atualiza o usuário atual e a lista de usuários não avaliados
            atualizar_usuario_e_usuarios_nao_avaliados(usuario_atual)
            # Verifica se ainda há usuários não avaliados
            if not usuarios_nao_avaliados:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação')
                break

            # Obtém o próximo usuário a ser avaliado
            proximo_usuario = obter_proximo_usuario()
            if proximo_usuario:
                # Define o layout da janela de avaliação
                avaliacao_layout = [
                    [sg.Text(f'Você está avaliando o usuário {proximo_usuario["nome"]}',
                            font=('Arial', 18), justification='center', background_color='white',
                            size=(30, 1),
                            relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
                    [sg.Text('Responda as seguintes perguntas:', font=('Arial', 18), size=(40, 1))]
                ]

                # Insere as perguntas
                for i, pergunta in enumerate(perguntas):
                    avaliacao_layout.append([
                        sg.Text(f'{i + 1}. {pergunta["pergunta"]}', font=('Arial', 18),
                                size=(40, 1)),
                        sg.Radio('0', f'resposta-{i}', default=False, size=(4, 1),
                                key=f'pergunta-{i}-opcao-0'),
                        sg.Radio('1', f'resposta-{i}', default=False, size=(4, 1),
                                key=f'pergunta-{i}-opcao-1'),
                        sg.Radio('2', f'resposta-{i}', default=False, size=(4, 1),
                                key=f'pergunta-{i}-opcao-2'),
                        sg.Radio('3', f'resposta-{i}', default=False, size=(4, 1),
                                key=f'pergunta-{i}-opcao-3')
                    ])

                # Adicionar o botão de enviar para a janela de avaliação
                avaliacao_layout.append(
                    [sg.Button('Enviar Avaliação', size=(20, 2), button_color=('white', 'black'),
                            font=('Helvetica', 20))])

                # Cria a janela de avaliação
                avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout,
                                            finalize=True, resizable=True,
                                            element_padding=(20, 20))
                # Definir o tamanho mínimo da janela
                avaliacao_janela.set_min_size((800, 600))

                # Atualiza o usuário atual e a janela principal
                usuario_atual = proximo_usuario
                window.close()
                window = avaliacao_janela

            else:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação', keep_on_top=True)
                break

