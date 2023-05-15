import PySimpleGUI as sg
import avaliacao

def seleciona_sprint(usuario):
    # Carrega um tema pré definido do PySimpleGui
    sg.theme('DefaultNoMoreNagging')

    # Define as imagens dos botões
    sprint1_button = sg.Button("Sprint 1", key='sprint-1', size=(20, 5),border_width=3)
    sprint2_button = sg.Button("Sprint 2", key='sprint-2', size=(20, 5),border_width=3)
    sprint3_button = sg.Button("Sprint 3", key='sprint-3', size=(20, 5),border_width=3)
    sprint4_button = sg.Button("Sprint 4", key='sprint-4', size=(20, 5),border_width=3)

    # Define o layout da janela principal
    layout = [
        [sg.Text('Selecione uma sprint para avaliar', font=('Arial', 20), justification='center', text_color='black',
                background_color='white', size=(30, 1), relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
        [sg.Column(layout=[[sprint1_button, sprint2_button]], justification='center', element_justification='center')],
        [sg.Column(layout=[[sprint3_button, sprint4_button]], justification='center', element_justification='center')]
    ]

    # Cria a janela principal
    window = sg.Window('Avaliação 360° - PBLTex', layout, finalize=True, resizable=True, element_padding=(25, 25))

    # Definir o tamanho mínimo da janela
    window.set_min_size((800, 600))

    # Loop de eventos
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "sprint-1":
            avaliacao.tela_avaliacao("1", usuario)
        elif event == "sprint-2":
            avaliacao.tela_avaliacao("2", usuario)
        elif event == "sprint-3":
            avaliacao.tela_avaliacao("3", usuario)
        elif event == "sprint-4":
            avaliacao.tela_avaliacao("4", usuario)
        else:
            continue

    # Fecha a janela principal
    window.close()
