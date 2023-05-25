import PySimpleGUI as sg
import json
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import numpy as np
import dashboard_2
matplotlib.use('TkAgg')


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
      # Carregar usuários do arquivo JSON
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

     # Layout da tela de resultado por usuário
    layout = [
        [sg.Text("Resultado por Usuário", font=("Helvetica", 16))],
            [
                sg.Text("Selecione o Usuário:", font=("Helvetica", 10)),
                sg.Listbox(values=[usuario["nome"] for usuario in usuarios], size=(30, 1), key="-LISTA-"),
                sg.Button("Confirmar", size=(10, 1), key="-SELECIONA_USUARIO-")
            ],
        [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por usuário
    window = sg.Window("Painel do Administrador", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-SELECIONA_USUARIO-":
            if len(values ["-LISTA-"]) > 0:
                usuario_selecionado = values ["-LISTA-"][0]
                tela_resultado_usuario_sprint(usuario_selecionado)
            else:
                sg.popup("Nenhum usuário selecionado!")


    window.close()

def tela_resultado_usuario_sprint(nome_usuario_selecionado):
       # Layout da tela de resultado usuário por sprint
    layout_aba_sprint1 = [
        [sg.Text("Resultado da Sprint 1", font=("Helvetica", 10))],
        [sg.Canvas(key='-CANVAS_SPRINT_1-')] 
    ]
    layout_aba_sprint2 = [
        [sg.Text("Resultado da Sprint 2", font=("Helvetica", 10))]  
    ]
    layout_aba_sprint3 = [
        [sg.Text("Resultado da Sprint 3", font=("Helvetica", 10))]  
    ]
    layout_aba_sprint4 = [
        [sg.Text("Resultado da Sprint 4", font=("Helvetica", 10))]  
    ]
    layout = [
        [sg.Text("Resultado de " + nome_usuario_selecionado, font=("Helvetica", 16))],
        [sg.TabGroup([[
            sg.Tab("Sprint 1", layout_aba_sprint1), 
            sg.Tab("Sprint 2", layout_aba_sprint2),
            sg.Tab("Sprint 3", layout_aba_sprint3),
            sg.Tab("Sprint 4", layout_aba_sprint4)    
        ]])],
        [sg.Button("Sair", size=(10, 1))]
    ]
      
    window = sg.Window("Painel do Administrador", layout, finalize=True)

    desenho_do_grafico_sprint1= dashboard_2.gerar_grafico_resultado_individual(1,buscar_usuario_por_nome(nome_usuario_selecionado))

    tkcanvas = desenhar_grafico_na_aba(window['-CANVAS_SPRINT_1-'].TKCanvas, desenho_do_grafico_sprint1)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break


    window.close()

def desenhar_grafico_na_aba(canvas, figure):
   tkcanvas = FigureCanvasTkAgg(figure, canvas)
   tkcanvas.draw()
   tkcanvas.get_tk_widget().pack(side='top', fill='both', expand=1)
   return tkcanvas

def buscar_usuario_por_nome(nome_usuario_selecionado):
    
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

    usuario_selecionado = ""
     # Procurar usuário pelo nome
    for usuario in usuarios:
        if usuario["nome"] == nome_usuario_selecionado:
            usuario_selecionado = usuario
    
    return usuario_selecionado


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




