import PySimpleGUI as sg
import csv
import json

# Carrega o conteúdo do arquivo data.json em um dicionário Python
with open('data.json', 'r') as f:
    data = json.load(f)

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

# Define as imagens dos botões
admin_button = sg.Button(key='admin', image_filename='admin.png', button_color=('white', 'white'), size=(300, 300), border_width=6)
user_button = sg.Button(key='user', image_filename='user.png', button_color=('white', 'white'), size=(300, 300), border_width=6)

# Define o layout da janela principal
layout = [
    [sg.Text('Escolha uma opção', font=('Arial', 20), justification='center', text_color='black', background_color='white', size=(30, 1), relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
    [sg.Column(layout=[[admin_button, user_button]], justification='center', element_justification='center')]
]

# Cria a janela principal
window = sg.Window('Avaliação 360° - PBLTex', layout, finalize=True, resizable=True, element_padding=(50,50))

# Definir o tamanho mínimo da janela
window.set_min_size((800,600))

# Variável para armazenar a janela de login do administrador
admin_window = None

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'admin':
        # Abre a janela de login do administrador
        admin_layout = [
            [sg.Text('Login do Administrador', font=('Helvetica', 30), justification='center')],
            [sg.Text('Senha:', font=('Helvetica', 20)), sg.InputText(password_char='*', font=('Helvetica', 20))],
            [sg.Button('Confirmar', font=('Helvetica', 20), button_color=('white', 'black'), size=(10, 1))]
        ]
        admin_window = sg.Window('Login do Administrador', admin_layout, element_justification='center')
        while True:
            event, values = admin_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Confirmar':
                # Valida a senha inserida pelo administrador
                senha = values[0]
                if senha == data['admin']['senha']:
                    # Define o layout da janela de gerenciamento
                    gerenciamento_layout = [
                        [sg.Text('Página de Gerenciamento', font=('Helvetica', 30), justification='center')],
                        # Aqui você pode adicionar outros elementos de layout que precisar para a janela de gerenciamento
                    ]
                    # Cria a janela de gerenciamento com o tamanho padrão da tela
                    gerenciamento_janela = sg.Window('Tela do Administrador', gerenciamento_layout,
                                                     finalize=True, resizable=True, element_padding=(50, 50),
                                                     keep_on_top=True)
                    # Definir o tamanho mínimo da janela
                    gerenciamento_janela.set_min_size((800, 600))

                else:
                    print("Senha incorreta. Tente novamente.")
                # Fecha a janela de login do administrador
                admin_window.close()
    elif event == 'user':
        # Abre a janela de login do usuário comum
        user_layout = [
            [sg.Text('Login do Usuário', font=('Helvetica', 30), justification='center')],
            [sg.Text('Matrícula:', font=('Helvetica', 20)), sg.InputText(font=('Helvetica', 20))],
            [sg.Button('Confirmar', font=('Helvetica', 20), button_color=('white', 'black'), size=(10, 1))]
        ]
        user_window = sg.Window('Login do Usuário Comum', user_layout, element_justification='center')
        while True:
            event, values = user_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Confirmar':
                # Valida a matrícula inserida pelo usuário comum
                matricula = values[0]
                for usuario in data['usuarios']:
                    if matricula == usuario['matricula']:
                        # Cria a janela de avaliação
                        perguntas = []
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
                            [sg.Text('Avaliação 360°', font=('Helvetica', 30), justification='center')],
                            [sg.Text('Por favor, avalie o usuário com base nas seguintes perguntas:',
                                        font=('Helvetica', 20),
                                        justification='center')],
                            [sg.Text('', size=(50, 1))],
                        ]

                        # Adiciona as perguntas e as opções de resposta ao layout
                        for i, pergunta in enumerate(perguntas):
                            pergunta_layout = [
                                sg.Text(f'{i + 1}. {pergunta["pergunta"]}', font=('Helvetica', 16))
                            ]
                            for j, opcao in enumerate(pergunta['opcoes']):
                                pergunta_layout.append(
                                    sg.Radio(opcao, "OPÇÕES", font=('Helvetica', 16), key=f'{i}_{j}'))

                            avaliacao_layout.append(pergunta_layout)

                        # Adiciona o botão de enviar
                        avaliacao_layout.append(
                            [sg.Button('Enviar Avaliação', size=(30, 2), button_color=('white', 'black'),
                                        font=('Helvetica', 20))])

                        # Cria a janela de avaliação com o tamanho padrão da tela
                        avaliacao_janela = sg.Window('Avaliação 360°', avaliacao_layout, resizable=True,
                                                        finalize=True, element_justification='center')
                        user_window.close()

                        # Loop de eventos para a janela de avaliação
                        while True:
                            event, values = avaliacao_janela.read()
                            if event == sg.WIN_CLOSED:
                                break
                            elif event == 'Enviar Avaliação':
                                # Código para enviar a avaliação...
                                # Fecha a janela de avaliação
                                avaliacao_janela.close()
                else:
                    print("Matrícula incorreta ou inexistente. Tente novamente.")
                # Fecha a janela de login do administrador
                user_window.close()
# Fecha a janela principal
window.close()
