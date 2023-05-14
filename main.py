import PySimpleGUI as sg
import csv
import json
import avaliacao
import admin
import login

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

# Define as imagens dos botões
admin_button = sg.Button(key='admin', image_filename='recursos/admin.png', button_color=('white', 'white'), size=(300, 300),
                         border_width=6)
user_button = sg.Button(key='user', image_filename='recursos/user.png', button_color=('white', 'white'), size=(300, 300),
                        border_width=6)

# Define o layout da janela principal
layout = [
    [sg.Text('Escolha uma opção', font=('Arial', 20), justification='center', text_color='black',
             background_color='white', size=(30, 1), relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
    [sg.Column(layout=[[admin_button, user_button]], justification='left', element_justification='center')]
]

# Cria a janela principal
window = sg.Window('Avaliação 360° - PBLTex', layout, finalize=True, resizable=True, element_padding=(50, 50))

# Definir o tamanho mínimo da janela
window.set_min_size((800, 600))

# Loop de eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'admin':
        # Abre a janela de login do administrador
        if (login.popup_login(event)):
            admin.tela_administracao()
        else:
            sg.popup("Senha incorreta!", title='Erro', keep_on_top=True)
        
    elif event == 'user':
        # Abre a janela de login do usuário comum
        usuario = login.popup_login(event)
        if (usuario):
            print(usuario)
            avaliacao.tela_avaliacao(1, usuario)
        else:
            sg.popup("Usuário não cadastrado!", title='Erro', keep_on_top=True)

# Fecha a janela principal
window.close()
