import PySimpleGUI as sg
import json
import db_json as dbj
import resultados

usuario = None
sprint = None
usuarios_nao_avaliados = []
usuario_atual = None
feedback = ''
perguntas = ["Engajamento e Pró-atividade",
             "Auto-gestão das Atividades",
             "Comunicação e Trabalho em Equipe",
             "Conhecimento e Aplicabilidade Técnica",
             "Entrega de Resultados com Valor Agregado"]

# Define a função para atualizar o usuário atual e a lista de usuários não avaliados
def atualizar_usuario_e_usuarios_nao_avaliados(usuario):
    global usuario_atual, usuarios_nao_avaliados
    usuario_atual = usuario
    usuarios_nao_avaliados = [u for u in usuarios_nao_avaliados if u['matricula'] != usuario['matricula']]

# Define a função para obter o próximo usuário a ser avaliado
def obter_proximo_usuario():
    for usuario in usuarios_nao_avaliados:
        if usuario['matricula'] != usuario_atual['matricula']:
            return usuario
    return None

def layout_questionario(layout):
    layout.append([sg.HSeparator(pad=(0,0))])

    layout.append([
        sg.Text(' ', font=('Arial', 12), size=(41, 1)),
        sg.Text('1', font=('Arial', 12), size=(3, 1)),
        sg.Text('2', font=('Arial', 12), size=(3, 1)),
        sg.Text('3', font=('Arial', 12), size=(3, 1)),
        sg.Text('4', font=('Arial', 12), size=(3, 1)),
        sg.Text('5', font=('Arial', 12), size=(3, 1)),
        ])
    
    layout.append([sg.HSeparator(pad=(0,0))])
    
    for i in range(0, len(perguntas)):
        layout.append([
            sg.Text(perguntas[i], font=('Arial', 12), size=(40, 1)),
            sg.Radio('', i, default=False, size=(1, 1), key=f"p{i}-opcao-1", background_color="#FF6347"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"p{i}-opcao-2", background_color="#EB8A41"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"p{i}-opcao-3", background_color="#D6B13B"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"p{i}-opcao-4", background_color="#C2D835"),
            sg.Radio('', i, default=False, size=(1, 1), key=f"p{i}-opcao-5", background_color="#ADFF2F")
        ])

    layout.append([sg.HSeparator(),sg.Text("1-Ruim, 2-Regular, 3-Bom, 4-Muito Bom, 5-Excelente")])

def layout_avaliacao(sprint, usuario):
    # Define o layout da janela de avaliação
    layout = []
    layout = [
        [sg.Text('Você está avaliando o usuário ' + usuario['nome'],
                font=('Arial', 18), justification='center', background_color='white', size=(40, 0),
                relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)]
                ,
       
    ]

    button_layout = [[sg.Button("Individual", key="individual", disabled=True, size=(10,2), button_color=('white', 'gray'))],
                    [sg.Button("Equipe", key="equipe", disabled=True, size=(10,2), button_color=('white', 'gray'))],
                    [sg.HSeparator()],
                    [sg.Button("Salvar", key="salvar", size=(10,2))],
                    [sg.Button("Minha\nAvaliação", key="avaliacao", size=(10,2))],
                    [sg.Button("Sair", key="sair", size=(10,2))]]

    # Insere o layout das perguntas
    questionario = []
    questionario.append([sg.Text('Nome: ' + usuario['nome'] +
                '        |        Sprint: ' + sprint +
                '        |        Turma: ' + usuario['turma'] +
                '        |        Time: ' + usuario['time'], font=('Arial', 14))])
    
    layout_questionario(questionario)
    #layout.append([sg.Frame('Avalie ' + nome, questionario)])

    layout.append([sg.Column(button_layout),
                   sg.VSeparator(),
                   sg.Column(questionario)
    ])

    # Adicionar o botão de enviar para a janela de avaliação
    layout.append(
    [sg.Button('Próximo', key='proximo', size=(20, 2),
                button_color=('white', 'black'),
                font=('Helvetica', 20),
                disabled=False)
                ])

    return layout

#Adiciona uma caixa de texto para dar feedback a cada usuario
def layout_feedback(feedback):
    layout = [
        [sg.Text('Feedback', font=('Arial', 18), justification='center', background_color='white', size=(40, 0),
                 relief=sg.RELIEF_RIDGE, border_width=2, expand_x=True)],
        [sg.Text(feedback, font=('Arial', 14), size=(40, 1))]
    ]
    return layout

# Função para obter as opções selecionadas
def opcoes_selecionadas(values):
    respostas = {}
    for i in range(0, len(perguntas)):
        for j in range(1, 6):
            if values[f"p{i}-opcao-{j}"] == True:
                respostas.update({f"p{i}": j})
    return respostas

def tela_feedback(sprint, usuario, usuario_atual):
    # Obtém o feedback atual que está armazenado no arquivo avaliacoes.json
    default_text = dbj.get_feedback(sprint, usuario, usuario_atual)

    layout_feedback = [
        [sg.Text(f'Você deu uma nota menor ou igual a 3, deixe seu feedback para {usuario_atual["nome"]}', size=(50, 2))], 
        [sg.Multiline(key="-FEEDBACK-", default_text=default_text, size=(52, 4))],
        [sg.Button("Salvar", size=(10, 1)), sg.Button('Cancelar', size=(10, 1))]
    ]

    window_feedback = sg.Window("Deixe seu feedback!", layout_feedback)

    while True:
        event_feedback, values_feedback = window_feedback.read()

        if event_feedback == "Salvar":
            feedback = values_feedback["-FEEDBACK-"]

            # Verifica se o campo de texto não está vazio
            if len(feedback) == 0:
                sg.Popup('É necessário deixar seu feedback para prosseguir!')
                continue

            # Persiste o feedback no arquivo avalicoes.json
            dbj.set_feedback(sprint, usuario, usuario_atual, feedback)
            break
        elif event_feedback == sg.WINDOW_CLOSED or event_feedback == 'Cancelar':
            break

    window_feedback.close()

def tela_avaliacao(sprint, usuario):
    global usuarios_nao_avaliados, usuario_atual
    print("Abrindo a tela de avaliação")

    # Carrega um tema pré definido do PySimpleGui
    sg.theme('DefaultNoMoreNagging')

    # Carrega o conteúdo do arquivo data.json em um dicionário Python
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    dbj.carrega_arquivo_json('avaliacoes.json')

    # Armazena a lista de usuários não avaliados
    usuarios_nao_avaliados = [usuario for usuario in data['usuarios'] if usuario['matricula'] != 'admin']

    atualizar_usuario_e_usuarios_nao_avaliados(usuario)
    
    # Criar uma lista para armazenar as respostas
    respostas = []

    avaliacao_layout = layout_avaliacao(sprint, usuario)

    # Cria a janela de avaliação
    avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout, finalize=True,
                            resizable=True, element_padding=(20, 20))

    # Habilita o botão da avaliação individual, o botão serve apenas para indicar que está
    # sendo feita a avaliação individual
    avaliacao_janela['individual'].update(disabled=False, button_color=('white', 'green'))

    # Definir o tamanho mínimo da janela
    avaliacao_janela.set_min_size((800, 600))

    avaliacao_janela_anterior = avaliacao_janela

    # Estrutura para armazenar temporariamente a avaliação
    avaliacao = {"tipo": "individual", "respostas": {}}
    
    respostas = dbj.get_respostas(sprint, usuario, usuario_atual)
    if respostas:
        for r in respostas:
            avaliacao_janela[f"{r}-opcao-{respostas[r]}"].update(True)


    # Loop de eventos da janela de avaliação
    feedback_ok = False
    while True:
        event, values = avaliacao_janela.read()

        # Verifica se foi dado uma nota menor ou igual a 3
        if event == 'proximo' or event == 'salvar':
            respostas = opcoes_selecionadas(values)

            for i in range(0, len(respostas)):
                # Caso tenha sido dado uma nota menor ou igual a 3 e não seja uma avaliação individual/pessoal
                if respostas[f'p{i}'] <= 3 and usuario != usuario_atual and feedback_ok == False:
                    tela_feedback(sprint, usuario, usuario_atual)
                    feedback_ok = True
                    break

        if event == sg.WIN_CLOSED:
            break

        # Limpa as opções elecionadas
        elif event == 'limpar':
            for i in range(0, len(perguntas)):
                for j in range(1, 6):
                    if values[f"p{i}-opcao-{j}"]:
                        avaliacao_janela[f'p{i}-opcao-{j}'].Update(False)
            continue

        elif event == 'proximo':
            # Obtém as opções selecionadas
            respostas = opcoes_selecionadas(values)

            if not usuarios_nao_avaliados:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação')
                break

            # Verifica se a quantidade de respostas é menor que a quantidade de perguntas
            if len(respostas) < len(perguntas):
                sg.popup("Preencha todas os tópicos antes de continuar")
                continue

            # Armazena a avaliação na estrutura definitiva que será salva no arquivo json posteriormente
            dbj.set_respostas(sprint, usuario, usuario_atual, respostas)

            # Cria uma nova estrutura temporária para armezenar a próxima avaliação
            avaliacao = {"tipo": "equipe", "respostas": {}}

            # Atualiza o usuário atual e a lista de usuários não avaliados
            atualizar_usuario_e_usuarios_nao_avaliados(usuario_atual)
            # Verifica se ainda há usuários não avaliados
            if not usuarios_nao_avaliados:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação')
                break

            # Obtém o próximo usuário a ser avaliado
            proximo_usuario = obter_proximo_usuario()
            if proximo_usuario:
                # Salva a avaliação atual
                dbj.set_respostas(sprint, usuario, usuario_atual, respostas)
                dbj.salva_arquivo_json('avaliacoes.json')
                feedback_ok = False

                avaliacao_layout = layout_avaliacao(sprint, proximo_usuario)

                # Cria a janela de avaliação
                avaliacao_janela = sg.Window('Avaliação 360° - PBLTex', avaliacao_layout,
                                            finalize=True, resizable=True,
                                            element_padding=(20, 20))
                
                # Habilita o botão da avaliação da equipe, o botão serve apenas para indicar que está
                # sendo feita a avaliação de um membro da equipe
                avaliacao_janela['equipe'].update(disabled=False, button_color=('white', 'green'))

                # Definir o tamanho mínimo da janela
                avaliacao_janela.set_min_size((800, 600))

                # Atualiza o usuário atual e a janela principal
                usuario_atual = proximo_usuario
                avaliacao_janela_anterior.close()
                avaliacao_janela_anterior = avaliacao_janela

                respostas = dbj.get_respostas(sprint, usuario, usuario_atual)
                if respostas:
                    for r in respostas:
                        avaliacao_janela[f"{r}-opcao-{respostas[r]}"].update(True)

            else:
                sg.popup('A avaliação foi concluída!', title='Fim da avaliação', keep_on_top=True)
                dbj.set_respostas(sprint, usuario, usuario_atual, respostas)
                dbj.salva_arquivo_json('avaliacoes.json')
                sg.popup('Sua avaliação foi salva!', title='Avaliação salva!', keep_on_top=True)
                break
        elif event == 'salvar':
            respostas = opcoes_selecionadas(values)
            dbj.set_respostas(sprint, usuario, usuario_atual, respostas)
            dbj.salva_arquivo_json('avaliacoes.json')
            sg.popup('Sua avaliação foi salva!', title='Avaliação salva!', keep_on_top=True)

        elif event == 'avaliacao':
            resultados.tela_resultado_usuario_feedback(sprint, usuario)
            continue
            
        elif event == 'sair':
            avaliacao_janela.close()
            break
