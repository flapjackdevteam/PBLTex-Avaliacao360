import PySimpleGUI as sg

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def tela_resultado():
      # Layout da tela de resultado
    layout = [
        [sg.Text("Resultado das avaliações", font=("Helvetica", 16))],
        [sg.Button("Resultado por Usuário", size=(20, 2), key="-RESULTADO_USUARIO-")],
        [sg.Button("Resultado por Time", size=(20, 2), key="-RESULTADO_TIME-")],
        [sg.Button("Resultado por Turma", size=(20, 2), key="-RESULTADO_TURMA-")],
        [sg.Button("Sair", size=(10, 1))]
    ]
    # Criação da janela da tela de resultados
    window = sg.Window("Painel do Administrador", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-RESULTADO_USUARIO-":
            tela_resultado_usuario()
        elif event == "-RESULTADO_TIME-":
            tela_resultado_time()
        elif event == "-RESULTADO_TURMA-":
            tela_resultado_turma()

    window.close()



def tela_resultado_usuario():
     # Layout da tela de resultado por usuário
    layout = [
        [sg.Text("Resultado por Usuário", font=("Helvetica", 16))],
          [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por usuário
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break

    window.close()

def tela_resultado_time():
     # Layout da tela de resultado por time
    layout = [
        [sg.Text("Resultado por Time", font=("Helvetica", 16))],
          [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por time
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break

    window.close()

def tela_resultado_turma():
     # Layout da tela de resultado por turma
    layout = [
        [sg.Text("Resultado por Turma", font=("Helvetica", 16))],
          [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por turma
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break

    window.close()




