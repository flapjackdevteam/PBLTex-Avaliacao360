import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging’')

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
                password = values[0]
                # Código para validar a senha...
                # Fecha a janela de login do administrador
                admin_window.close()
    elif event == 'user':
        # Abre a janela de login do usuário comum
        user_layout = [
            [sg.Text('Login do Usuário Comum', font=('Helvetica', 30), justification='center')],
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
                # Código para validar a matrícula...
                # Fecha a janela de login do usuário comum
                user_window.close()

# Fecha a janela principal
window.close()
