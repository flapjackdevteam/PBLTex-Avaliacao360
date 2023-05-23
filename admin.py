import PySimpleGUI as sg
import json

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def tela_administracao():
    # Layout da tela de administração
    layout = [
        [sg.Text("Gerenciamento do Administrador", font=("Helvetica", 16))],
        [sg.Button("Adicionar usuário", size=(20, 2), key="-ADICIONAR-")],
        [sg.Button("Selecionar usuário", size=(20, 2), key="-SELECIONAR-")],
        [sg.Button("Sair", size=(10, 1))]
    ]

    # Criação da janela da tela de administração
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-ADICIONAR-":
            adicionar_usuario()
        elif event == "-SELECIONAR-":
            selecionar_usuario()

    window.close()

# Solicitar informações do novo usuário
def adicionar_usuario():
    layout_admin = [
        [sg.Text("Nome:      "), sg.Input(key="-NOME-", border_width=2, size=(25, 1))],
        [sg.Text("Matrícula: "), sg.Input(key="-MATRICULA-", border_width=2, size=(17, 1))],
        [sg.Text("Turma:     "), sg.Input(key="-TURMA-", border_width=2, size=(10, 1))],
        [sg.Text("Times:     "), sg.Input(key="-TIMES-", border_width=2, size=(10, 1))],
        [sg.Button("Adicionar", size=(10, 1))]
    ]

    window_admin = sg.Window("Adicionar Usuário", layout_admin)

    while True:
        event_admin, values_admin = window_admin.read()

        if event_admin == sg.WINDOW_CLOSED or event_admin == "Adicionar":
            break

    window_admin.close()

    # Carregar usuários existentes do arquivo JSON
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

    # Criar usuário com as informações digitadas
    novo_usuario = {
        "nome": values_admin["-NOME-"],
        "matricula": values_admin["-MATRICULA-"],
        "turma": values_admin["-TURMA-"],
        "times": values_admin["-TIMES-"]
    }

    # Adicionar o novo usuário à lista existente
    usuarios.append(novo_usuario)

    # Salvar a lista de usuários atualizada no arquivo JSON
    with open("data.json", "w") as arquivo:
        json.dump(data, arquivo)

    sg.popup("Usuário adicionado com sucesso!")

def editar_usuario(nome_usuario):
    # Carregar usuários do arquivo JSON
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

    # Procurar usuário pelo nome
    for usuario in usuarios:
        if usuario["nome"] == nome_usuario:
            # Solicitar novas informações do usuário
            layout_admin = [
                [sg.Text("Novo nome: "), sg.Input(key="-NOVO_NOME-", default_text=usuario["nome"])],
                [sg.Text("Nova matrícula: "), sg.Input(key="-NOVA_MATRICULA-", default_text=usuario["matricula"])],
                [sg.Button("Atualizar")]
            ]

            window_admin = sg.Window("Editar Usuário", layout_admin)

            while True:
                event_admin, values_admin = window_admin.read()

                if event_admin == sg.WINDOW_CLOSED or event_admin == "Atualizar":
                    break

            window_admin.close()

            # Atualizar informações do usuário
            usuario["nome"] = values_admin["-NOVO_NOME-"]
            usuario["matricula"] = values_admin["-NOVA_MATRICULA-"]

            # Salvar usuários atualizados no arquivo JSON
            with open("data.json", "w") as arquivo:
                json.dump(data, arquivo)

            sg.popup("Usuário atualizado com sucesso!")
            return

    sg.popup("Usuário não encontrado!")

def remover_usuario(nome_usuario):
    # Carregar usuários do arquivo JSON
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

    # Procurar usuário pelo nome
    for usuario in usuarios:
        if usuario["nome"] == nome_usuario:
            usuarios.remove(usuario)

            # Salvar usuários atualizados no arquivo JSON
            with open("data.json", "w") as arquivo:
                json.dump(data, arquivo)

            sg.popup("Usuário removido com sucesso!")
            return

    sg.popup("Usuário não encontrado!")

def selecionar_usuario():
    # Carregar usuários do arquivo JSON
    with open("data.json", "r") as arquivo:
        data = json.load(arquivo)

    usuarios = data["usuarios"]

    # Criar layout da lista de usuários
    layout_lista = [
        [sg.Listbox(values=[usuario["nome"] for usuario in usuarios], size=(30, 6), key="-LISTA-")],
        [sg.Button("Editar", key="-EDITAR-"), sg.Button("Remover", key="-REMOVER-")]
    ]

    window_lista = sg.Window("Selecione um Usuário", layout_lista)

    while True:
        event_lista, values_lista = window_lista.read()

        if event_lista == sg.WINDOW_CLOSED:
            break
        elif event_lista == "-EDITAR-":
            # Verificar se um usuário foi selecionado
            if len(values_lista["-LISTA-"]) > 0:
                usuario_selecionado = values_lista["-LISTA-"][0]
                editar_usuario(usuario_selecionado)
                break
            else:
                sg.popup("Nenhum usuário selecionado!")
        elif event_lista == "-REMOVER-":
            # Verificar se um usuário foi selecionado
            if len(values_lista["-LISTA-"]) > 0:
                usuario_selecionado = values_lista["-LISTA-"][0]
                remover_usuario(usuario_selecionado)
                break
            else:
                sg.popup("Nenhum usuário selecionado!")

    window_lista.close()


# Layout da interface
layout = [
    [sg.Text("Gerenciamento do Administrador", font=("Helvetica", 16))],
    [sg.Button("Adicionar usuário", size=(20, 2), key="-ADICIONAR-")],
    [sg.Button("Selecionar usuário", size=(20, 2), key="-SELECIONAR-")],
    [sg.Button("Sair", size=(10, 1))]
]

# Criação da janela
window = sg.Window("Painel do Administrador", layout)

# Loop de eventos da janela
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Sair":
        break
    elif event == "-ADICIONAR-":
        adicionar_usuario()
    elif event == "-SELECIONAR-":
        selecionar_usuario()

window.close()
