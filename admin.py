import PySimpleGUI as sg
import json
import resultados
import db_json as dbj

# Carrega um tema pré definido do PySimpleGui
sg.theme('DefaultNoMoreNagging')

def tela_administracao():
    # Layout da tela de administração
    layout = [
        [sg.Text("Gerenciamento do Administrador", font=("Helvetica", 16))],
        [sg.Button("Adicionar usuário", size=(20, 2), key="-ADICIONAR-")],
        [sg.Button("Selecionar usuário", size=(20, 2), key="-SELECIONAR-")],
        [sg.Button("Configurar Sprints", size=(20, 2), key="-CONFIGURAR_SPRINTS-")],
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
        elif event == "-CONFIGURAR_SPRINTS-":
            configurar_sprints()

    window.close()

def configurar_sprints():
    qtd_de_sprints = dbj.get_qtd_de_sprints()

    layout_config_sprints = [
        [sg.Text("Quantidade de Sprints:", size=(18, 1)), sg.Input(key="-SPRINTS-", default_text=str(qtd_de_sprints), size=(10, 1))],
        [sg.Button("Salvar", size=(10, 1))]
    ]

    window_config_sprints = sg.Window("Configurar Sprints", layout_config_sprints)

    while True:
        event_config_sprints, values_config_sprints = window_config_sprints.read()

        if event_config_sprints == "Salvar":
            # Persiste a quantidade de sprints
            qtd_de_sprints = int(values_config_sprints["-SPRINTS-"])
            dbj.set_qtd_de_sprints(qtd_de_sprints)

            sg.popup(f"Quantidade de Sprints configurada para: {qtd_de_sprints}")
            break
        elif event_config_sprints == sg.WINDOW_CLOSED:
            break

    window_config_sprints.close()

# Solicitar informações do novo usuário
def adicionar_usuario():
    layout_admin = [
        [sg.Text("Nome:      "), sg.Input(key="-NOME-", border_width=2, size=(25, 1))],
        [sg.Text("Matrícula: "), sg.Input(key="-MATRICULA-", border_width=2, size=(17, 1))],
        [sg.Text("Turma:     "), sg.Input(key="-TURMA-", border_width=2, size=(10, 1))],
        [sg.Text("Time:     "), sg.Input(key="-TIME-", border_width=2, size=(10, 1))],
        [sg.Button("Adicionar"), sg.Button("Cancelar")]
    ]

    window_admin = sg.Window("Adicionar Usuário", layout_admin)

    while True:
        event_admin, values_admin = window_admin.read()

        if event_admin == "Adicionar":
            # Carregar usuários existentes do arquivo JSON
            with open("data.json", "r") as arquivo:
                data = json.load(arquivo)

            # Criar usuário com as informações digitadas
            novo_usuario = {
                "nome": values_admin["-NOME-"],
                "matricula": values_admin["-MATRICULA-"],
                "turma": values_admin["-TURMA-"],
                "time": values_admin["-TIME-"]
            }

            if dbj.ra_exist(novo_usuario['matricula']):
                sg.Popup('Já existe esse número de matrícula cadastrado!')
                continue

            # Adiciona o novo usuário na variável data
            data['usuarios'].append({'matricula': novo_usuario['matricula'],
                                    'nome': novo_usuario['nome'],
                                    'turma': novo_usuario['turma'],
                                    'time': novo_usuario['time']})

            # Salvar a lista de usuários atualizada no arquivo JSON
            with open("data.json", "w") as arquivo:
                json.dump(data, arquivo, indent= 4)

            sg.popup("Usuário adicionado com sucesso!")
            break
        elif event_admin == sg.WINDOW_CLOSED or event_admin == "Cancelar":
            break

    window_admin.close()

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
                [sg.Text("Nova turma: "), sg.Input(key="-NOVA_TURMA-", default_text=usuario["turma"])],
                [sg.Text("Novo time: "), sg.Input(key="-NOVO_TIME-", default_text=usuario["time"])],
                [sg.Button("Atualizar"), sg.Button("Cancelar")]
            ]

            window_admin = sg.Window("Editar Usuário", layout_admin)

            while True:
                event_admin, values_admin = window_admin.read()

                if event_admin == event_admin == "Atualizar":
                    # Atualizar informações do usuário
                    usuario["nome"] = values_admin["-NOVO_NOME-"]
                    usuario["matricula"] = values_admin["-NOVA_MATRICULA-"]
                    usuario["turma"] = values_admin["-NOVA_TURMA-"]
                    usuario["time"] = values_admin["-NOVO_TIME-"]

                    # Salvar usuários atualizados no arquivo JSON
                    with open("data.json", "w") as arquivo:
                        json.dump(data, arquivo, indent=4)

                    sg.popup("Usuário atualizado com sucesso!")
                    break
                elif event_admin == sg.WINDOW_CLOSED or event_admin == "Cancelar":
                    break

            window_admin.close()
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
                json.dump(data, arquivo, indent=4)

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

def tela_opcoes_administracao():
    # Layout da tela de administração
    layout = [
        [sg.Text("Gerenciamento do Administrador", font=("Helvetica", 16))],
        [sg.Button("Gerenciamento de usuários", size=(20, 2), key="-GERENCIAMENTO_USUARIOS-")],
        [sg.Button("Visualizar resultados", size=(20, 2), key="-VER_RESULTADO-")],
        [sg.Button("Sair", size=(10, 1))]
    ]
     # Criação da janela da tela de administração
    window = sg.Window("Painel do Administrador", layout)

    # Loop de eventos da janela
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Sair":
            break
        elif event == "-GERENCIAMENTO_USUARIOS-":
            tela_administracao()
        elif event == "-VER_RESULTADO-":
            resultados.tela_resultado()


    window.close()
