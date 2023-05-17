import PySimpleGUI as sg
import csv
import json

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def adicionar_usuario():
    # Lógica para adicionar um usuário
    print("Adicionar usuário")

def remover_usuario():
    # Lógica para remover um usuário
    print("Remover usuário")

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
        [sg.Text("Gerenciamento do Administrador", font=("Helvetica", 16))],
        [sg.Button("Adicionar usuário", size=(20, 2),border_width=3)],
        [sg.Button("Remover usuário", size=(20, 2),border_width=3)],
        [sg.Button("Sair", size=(20, 2),border_width=3)]
        # Aqui você pode adicionar outros elementos de layout para a janela de gerenciamento
]

# Cria a janela de gerenciamento com o tamanho padrão da tela
gerenciamento_janela = sg.Window('Tela do Administrador', gerenciamento_layout,
                                    finalize=True, resizable=True, element_padding=(50, 50),
                                    keep_on_top=True)
 
 # Definir o tamanho mínimo da janela
gerenciamento_janela.set_min_size((800, 600))

# Loop para interagir com os eventos da janela
while True:
    event, values = gerenciamento_janela.read()

    # Se o usuário fechar a janela ou clicar em "Sair"
    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    # Se o usuário clicar em "Adicionar usuário"
    elif event == "Adicionar usuário":
        adicionar_usuario()
    # Se o usuário clicar em "Remover usuário"
    elif event == "Remover usuário":
        remover_usuario()

# Fechar a janela quando sair do loop
gerenciamento_janela.close()

