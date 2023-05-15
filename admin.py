import PySimpleGUI as sg
import csv
import json

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def tela_administracao():
    print("Abrindo a tela de administração!")

    # Carrega o conteúdo do arquivo data.json em um dicionário Python
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    admin_layout = [
            [sg.Text('Login do Administrador', font=('Helvetica', 30), justification='center')],
            [sg.Text('Senha:', font=('Helvetica', 20)), sg.InputText(password_char='*', font=('Helvetica', 20))],
            [sg.Button('Confirmar', font=('Helvetica', 20), button_color=('white', 'black'), size=(10, 1))]
        ]

    gerenciamento_layout = [
        [sg.Text('Página de Gerenciamento', font=('Helvetica', 30), justification='center')],
        # Aqui você pode adicionar outros elementos de layout para a janela de gerenciamento
    ]
    # Cria a janela de gerenciamento com o tamanho padrão da tela
    gerenciamento_janela = sg.Window('Tela do Administrador', gerenciamento_layout,
                                    finalize=True, resizable=True, element_padding=(50, 50),
                                    keep_on_top=True)
    # Definir o tamanho mínimo da janela
    gerenciamento_janela.set_min_size((800, 600))