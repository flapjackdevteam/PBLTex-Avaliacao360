import PySimpleGUI as sg
import csv
import json

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def popup_login(tipo):
    print("Abrindo a popup de login " + tipo)

    # Carrega o conteúdo do arquivo data.json em um dicionário Python
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    if tipo == 'admin':
        admin_layout = [
            [sg.Text('Login do Administrador', font=('Helvetica', 30), justification='center')],
            [sg.Text('Senha:', font=('Helvetica', 20)), sg.InputText(password_char='*', font=('Helvetica', 20))],
            [sg.Button('Confirmar', font=('Helvetica', 20), button_color=('white', 'black'), size=(10, 1))]
        ]

        # Abre a janela de login do administrador
        admin_window = sg.Window('Login do Administrador', admin_layout, element_justification='center')
        while True:
            event, values = admin_window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Confirmar':
                # Valida a senha inserida pelo administrador
                senha = values[0]
                admin_window.close()
                if senha == data['admin']['senha']:
                    # Define o layout da janela de gerenciamento
                    return True
                else:
                    return False
    else:
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

                user_window.close()
                for usuario in data['usuarios']:
                    if matricula == usuario['matricula']:
                        # Atualiza o usuário atual e a lista de usuários não avaliados
                        return usuario
                return None
            else:
                return None
            # Fecha a janela de login do administrador
            user_window.close()
        