import PySimpleGUI as sg
import avaliacao
import sys

def seleciona_sprint(usuario, qtd_de_sprints):
    # Carrega um tema pré definido do PySimpleGui
    sg.theme('DefaultNoMoreNagging')

    # Cria um layout para permitir selecionar a sprint desejada
    layout_lista = [[sg.Text('Selecione a sprint que deseja realizar a avalliação.')],
        [sg.Listbox(values=[i for i in range(1, qtd_de_sprints + 1)], size=(23, 3), key='-LISTA-')],
        [sg.Button('Selecionar', key='-SELECIONAR-'), sg.Button('Cancelar', key='-CANCELAR-')]
    ]

    # Cria a janela principal
    window = sg.Window('Avaliação 360° - PBLTex', layout_lista, element_justification='center')

    # Loop de eventos
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-CANCELAR-':
            break
        elif event == '-SELECIONAR-':
            sprint = str(values['-LISTA-'][0])
            avaliacao.tela_avaliacao(sprint, usuario)

    # Fecha a janela principal
    window.close()

# O código abaixo serve apeans para propósitos de debug
gettrace = getattr(sys, 'gettrace', None)

if gettrace():
    seleciona_sprint({'nome': 'Fátima Leise', 'matricula': '1460282313001'}, 10)
