import PySimpleGUI as sg
import json
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import numpy as np
import dashboard
import db_json as dbj

matplotlib.use('TkAgg')

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
    window = sg.Window("Painel do Administrador", layout, finalize=True,
                            resizable=True)

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
    qtd_sprints = dbj.get_qtd_de_sprints()
    layout_aba = []
    for i in range(1, qtd_sprints + 1):
        layout_aba.append(sg.Tab('Sprint ' + str(i), [
                [sg.Text("Resultado da Sprint " + str(i), font=("Helvetica", 10))],
                [sg.Canvas(key='-CANVAS_SPRINT_' + str(i) + '-')]]))
    font_size = 11

    layout_legendas = [sg.Column([[sg.Text('EPA: Engajamento e Pró-atividade', font=('Arial', font_size))],
                                  [sg.Text('AA: Auto-gestão das Atividades', font=('Arial', font_size))],
                                  [sg.Text('CTE: Comunicação e Trabalho em Equipe', font=('Arial', font_size))]]),
                       sg.VSeparator(),
                       sg.Column([[sg.Text('CAT: Conhecimento e Aplicabilidade Técnica', font=('Arial', font_size))],
                                  [sg.Text('ERVA: Entrega de Resultados com Valor Agregado', font=('Arial', font_size))]], vertical_alignment='Top')
    ]
    layout = [
        [sg.Text("Resultado de " + nome_usuario_selecionado, font=("Helvetica", 16))],
        [sg.TabGroup([layout_aba])],layout_legendas,
        [sg.Button("Sair", size=(10, 1))]
    ]
      
    window = sg.Window("Painel do Administrador", layout, finalize=True)

    usuario_alvo = buscar_usuario_por_nome(nome_usuario_selecionado)

    for i in range(1, qtd_sprints + 1):
        desenho_do_grafico = dashboard.gerar_grafico_resultado_individual(i, usuario_alvo)
        desenhar_grafico_na_aba(window['-CANVAS_SPRINT_' + str(i) + '-'].TKCanvas, desenho_do_grafico)
    
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

    lista_de_times= dbj.get_times()
     # Layout da tela de resultado por time
    layout = [
        [sg.Text("Resultado por Time", font=("Helvetica", 16))],
        [
                sg.Text("Selecione o Time:", font=("Helvetica", 10)),
                sg.Listbox(values= [time for time in lista_de_times], size=(30, 1), key="-LISTA-"),
                sg.Button("Confirmar", size=(10, 1), key="-SELECIONA_TIME-")
            ],
          [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por time
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-SELECIONA_TIME-":
            if len(values ["-LISTA-"]) > 0:
                time_selecionado = values ["-LISTA-"][0]
                tela_resultado_time_sprint(time_selecionado)
            else:
                sg.popup("Nenhum time selecionado!")


    window.close()

def tela_resultado_turma():
     # Layout da tela de resultado por turma
    lista_de_turma= dbj.get_turmas()
     # Layout da tela de resultado por time
    layout = [
        [sg.Text("Resultado por Turma", font=("Helvetica", 16))],
        [
                sg.Text("Selecione o Time:", font=("Helvetica", 10)),
                sg.Listbox(values= [turma for turma in lista_de_turma], size=(30, 1), key="-LISTA-"),
                sg.Button("Confirmar", size=(10, 1), key="-SELECIONA_TURMA-")
            ],
          [sg.Button("Sair", size=(10, 1))]
    ]
      # Criação da janela da tela de resultado por turma
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-SELECIONA_TURMA-":
            if len(values ["-LISTA-"]) > 0:
                turma_selecionado = values ["-LISTA-"][0]
                tela_resultado_turma_sprint(turma_selecionado)
            else:
                sg.popup("Nenhuma turma selecionada!")


    window.close()

def tela_resultado_time_sprint(time):
    # Layout da tela de resultado usuário por sprint
    qtd_sprints = dbj.get_qtd_de_sprints()
    layout_aba = []
    for i in range(1, qtd_sprints + 1):
        layout_aba.append(sg.Tab('Sprint ' + str(i), [
                [sg.Text("Resultado da Sprint " + str(i), font=("Helvetica", 10))],
                [sg.Canvas(key='-CANVAS_SPRINT_' + str(i) + '-')]]))
        
    font_size = 11
    layout_legendas = [sg.Column([[sg.Text('EPA: Engajamento e Pró-atividade', font=('Arial', font_size))],
                                  [sg.Text('AA: Auto-gestão das Atividades', font=('Arial', font_size))],
                                  [sg.Text('CTE: Comunicação e Trabalho em Equipe', font=('Arial', font_size))]]),
                       sg.VSeparator(),
                       sg.Column([[sg.Text('CAT: Conhecimento e Aplicabilidade Técnica', font=('Arial', font_size))],
                                  [sg.Text('ERVA: Entrega de Resultados com Valor Agregado', font=('Arial', font_size))]], vertical_alignment='Top')
    ]
    layout = [
        [sg.Text("Resultado do time " + time, font=("Helvetica", 16))],
        [sg.TabGroup([layout_aba])],layout_legendas,
        [sg.Button("Sair", size=(10, 1))]
    ]
      
    window = sg.Window("Painel do Administrador", layout, finalize=True)

    for i in range(1, qtd_sprints + 1):
        desenho_do_grafico = dashboard.gerar_grafico_resultado_time(i, time)
        desenhar_grafico_na_aba(window['-CANVAS_SPRINT_' + str(i) + '-'].TKCanvas, desenho_do_grafico)
    
    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break


    window.close()

    
def tela_resultado_turma_sprint(turma):
    # Layout da tela de resultado usuário por sprint
    qtd_sprints = dbj.get_qtd_de_sprints()
    layout_aba = []
    for i in range(1, qtd_sprints + 1):
        layout_aba.append(sg.Tab('Sprint ' + str(i), [
                [sg.Text("Resultado da Sprint " + str(i), font=("Helvetica", 10))],
                [sg.Canvas(key='-CANVAS_SPRINT_' + str(i) + '-')]]))

    font_size = 11
    layout_legendas = [sg.Column([[sg.Text('EPA: Engajamento e Pró-atividade', font=('Arial', font_size))],
                                  [sg.Text('AA: Auto-gestão das Atividades', font=('Arial', font_size))],
                                  [sg.Text('CTE: Comunicação e Trabalho em Equipe', font=('Arial', font_size))]]),
                       sg.VSeparator(),
                       sg.Column([[sg.Text('CAT: Conhecimento e Aplicabilidade Técnica', font=('Arial', font_size))],
                                  [sg.Text('ERVA: Entrega de Resultados com Valor Agregado', font=('Arial', font_size))]], vertical_alignment='Top')
    ]
    layout = [
        [sg.Text("Resultado da turma " + turma, font=("Helvetica", 16))],
        [sg.TabGroup([layout_aba])],layout_legendas,
        [sg.Button("Sair", size=(10, 1))]
    ]
      
    window = sg.Window("Painel do Administrador", layout, finalize=True)

    for i in range(1, qtd_sprints + 1):
        desenho_do_grafico = dashboard.gerar_grafico_resultado_turma(i, turma)
        desenhar_grafico_na_aba(window['-CANVAS_SPRINT_' + str(i) + '-'].TKCanvas, desenho_do_grafico)
    
    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break

    window.close()


