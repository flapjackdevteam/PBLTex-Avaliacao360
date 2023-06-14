import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import db_json as dbj

# Remove a barra de feramentas do matplotlib
plt.rcParams['toolbar'] = 'None'

# Função para plotar o dashboard de um usuário baseado na sprint informada
def gerar_grafico_resultado_individual(sprint, usuario):
    figure = plt.figure(figsize=(7, 4))
    """ MANIPULAÇÃO DOS DADOS
    Manipulação dos dados para transformar os dados armazenados em formato json em
    um dataframe contendo apenas as informações necessárias para obter a média das
    avaliações de um usuário"""

    # Carrega todo o conteúdo das avaliações na variável data
    data = dbj.get_json_data()

    # Converte o conteúdo json que está em data em dataframe normalizando a
    # sub-estrutira json Avaliacoes que está aninhada nos elementos do json
    # de avaliacoes.json mantendo os elementos RA1 e Sprint
    df = pd.json_normalize(data, 'Avaliacoes', ['RA1', 'Sprint'])

    # Renomeia as colunas das competencias para facilitar a manipulação dos dados
    df.rename(columns={'Respostas.p0': 'EPA',
                       'Respostas.p1': 'AA',
                       'Respostas.p2': 'CTE',
                       'Respostas.p3': 'CAT',
                       'Respostas.p4': 'ERVA'},
              inplace=True)

    matricula = usuario['matricula']

    # Filtra apenas as avaliações do usuário e sprint que desejo
    df = df.query(f'RA2 == "{matricula}" and Sprint == "{sprint}"')

    # Agrupa pelo RA2 e agrego pelas colunas EPA, AA, CTE, ERVA calculando suas médias (mean)
    df = df.groupby('RA2')[['EPA', 'AA', 'CTE', 'CAT', 'ERVA']].aggregate('mean').reset_index()

    # Multiplica o valor das colunas das competências apenas ajustar na exibição
    df['EPA'] *= 10
    df['AA']  *= 10
    df['CTE'] *= 10
    df['CAT'] *= 10
    df['ERVA']*= 10
    df.dropna(inplace=True)

    # Elimino registros que não há média, casos em que o usuário salvou a avaliação em branco
    if df.empty:
        figure, ax = plt.subplots(figsize=(7, 4))

        # Build a rectangle in axes coords
        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height

        ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'Não há dados referente a essa sprint!',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
        ax.set_axis_off()
    else:
        """ PLOTAGEM DO GRÁFICO
        O código abaixo é utilizado apenas para plotar o gráfico a partir do dataframe criado com os
        dados manipulados para a obtensão da média das avaliações de um usuário. """
        
        # Crio uma lista de categorias
        categories=list(df)[1:]

        # Obtenho o número total de categorias
        N = len(categories)
        
        # Crio uma lista com os valores das competências excluindo a coluna RA2
        # que não será necessário exibir no gráfico
        values=df.loc[0].drop('RA2').values.flatten().tolist()
        values += values[:1]

        # Cria uma lista com os angulos de potagem de acordo com a quantidade de categorias
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        ax = plt.subplot(111, polar=True)
        
        # Adiciona as categorias como marcações no gráfico
        plt.xticks(angles[:-1], categories, color='grey', size=10)
        
        # Inclui a marcação de valor que cada linha representa no gráfico
        ax.set_rlabel_position(0)
        plt.yticks([10,20,30,40,50], ["1","2","3","4","5"], color="grey", size=8)
        plt.ylim(0,50)
        
        # Plota um poligno interligando os pontos de avaliação
        ax.plot(angles, values, linewidth=1, linestyle='solid')
        # Preenche a área formada pelo poligono
        ax.fill(angles, values, 'b', alpha=0.1)

    # Retorna a figura do gráfico
    return figure

def gerar_grafico_resultado_time(sprint, time):
    figure = plt.figure(figsize=(7, 4))
    """ MANIPULAÇÃO DOS DADOS
    Manipulação dos dados para transformar os dados armazenados em formato json em
    um dataframe contendo apenas as informações necessárias para obter a média das
    avaliações de um usuário"""

    # Carrega todo o conteúdo das avaliações na variável data
    data = dbj.get_json_data()

    # Converte o conteúdo json que está em data em dataframe normalizando a
    # sub-estrutira json Avaliacoes que está aninhada nos elementos do json
    # de avaliacoes.json mantendo os elementos RA1 e Sprint
    df = pd.json_normalize(data, 'Avaliacoes', ['RA1', 'Sprint'])

    # Renomeia as colunas das competencias para facilitar a manipulação dos dados
    df.rename(columns={'Respostas.p0': 'EPA',
                       'Respostas.p1': 'AA',
                       'Respostas.p2': 'CTE',
                       'Respostas.p3': 'CAT',
                       'Respostas.p4': 'ERVA'},
              inplace=True)


    # Filtra apenas as avaliações do usuário e sprint que desejo
    df = df.query(f'time == "{time}" and Sprint == "{sprint}"')

    # Agrupa pelo RA2 e agrego pelas colunas EPA, AA, CTE, ERVA calculando suas médias (mean)
    df = df.groupby('time')[['EPA', 'AA', 'CTE', 'CAT', 'ERVA']].aggregate('mean').reset_index()

    # Multiplica o valor das colunas das competências apenas ajustar na exibição
    df['EPA'] *= 10
    df['AA']  *= 10
    df['CTE'] *= 10
    df['CAT'] *= 10
    df['ERVA']*= 10

    # Elimino registros que não há média, casos em que o usuário salvou a avaliação em branco
    if df.empty:
        figure, ax = plt.subplots(figsize=(7, 4))

        # Build a rectangle in axes coords
        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height

        ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'Não há dados referente a essa sprint!',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
        ax.set_axis_off()
    else:
        df.dropna(inplace=True)

        """ PLOTAGEM DO GRÁFICO
        O código abaixo é utilizado apenas para plotar o gráfico a partir do dataframe criado com os
        dados manipulados para a obtensão da média das avaliações de um usuário. """
        
        # Crio uma lista de categorias
        categories=list(df)[1:]

        # Obtenho o número total de categorias
        N = len(categories)
        
        # Crio uma lista com os valores das competências excluindo a coluna RA2
        # que não será necessário exibir no gráfico
        values=df.loc[0].drop('time').values.flatten().tolist()
        values += values[:1]

        # Cria uma lista com os angulos de potagem de acordo com a quantidade de categorias
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        ax = plt.subplot(111, polar=True)
        
        # Adiciona as categorias como marcações no gráfico
        plt.xticks(angles[:-1], categories, color='grey', size=10)
        
        # Inclui a marcação de valor que cada linha representa no gráfico
        ax.set_rlabel_position(0)
        plt.yticks([10,20,30,40,50], ["1","2","3","4","5"], color="grey", size=8)
        plt.ylim(0,50)
        
        # Plota um poligno interligando os pontos de avaliação
        ax.plot(angles, values, linewidth=1, linestyle='solid')
        # Preenche a área formada pelo poligono
        ax.fill(angles, values, 'b', alpha=0.1)

    # Retorna a figura do gráfico
    return figure


def gerar_grafico_resultado_turma(sprint, turma):
    figure = plt.figure(figsize=(7, 4))
    """ MANIPULAÇÃO DOS DADOS
    Manipulação dos dados para transformar os dados armazenados em formato json em
    um dataframe contendo apenas as informações necessárias para obter a média das
    avaliações de um usuário"""

    # Carrega todo o conteúdo das avaliações na variável data
    data = dbj.get_json_data()

    # Converte o conteúdo json que está em data em dataframe normalizando a
    # sub-estrutira json Avaliacoes que está aninhada nos elementos do json
    # de avaliacoes.json mantendo os elementos RA1 e Sprint
    df = pd.json_normalize(data, 'Avaliacoes', ['RA1', 'Sprint'])
    print(df)

    # Renomeia as colunas das competencias para facilitar a manipulação dos dados
    df.rename(columns={'Respostas.p0': 'EPA',
                       'Respostas.p1': 'AA',
                       'Respostas.p2': 'CTE',
                       'Respostas.p3': 'CAT',
                       'Respostas.p4': 'ERVA'},
              inplace=True)


    # Filtra apenas as avaliações do turma e sprint que desejo
    df = df.query(f'turma == "{turma}" and Sprint == "{sprint}"')

    # Agrupa pelo RA2 e agrego pelas colunas EPA, AA, CTE, ERVA calculando suas médias (mean)
    df = df.groupby('turma')[['EPA', 'AA', 'CTE', 'CAT', 'ERVA']].aggregate('mean').reset_index()

    # Multiplica o valor das colunas das competências apenas ajustar na exibição
    df['EPA'] *= 10
    df['AA']  *= 10
    df['CTE'] *= 10
    df['CAT'] *= 10
    df['ERVA']*= 10

    # Elimino registros que não há média, casos em que o usuário salvou a avaliação em branco
    if df.empty:
        figure, ax = plt.subplots(figsize=(7, 4))

        # Build a rectangle in axes coords
        left, width = .25, .5
        bottom, height = .25, .5
        right = left + width
        top = bottom + height

        ax.text(0.5 * (left + right), 0.5 * (bottom + top), 'Não há dados referente a essa sprint!',
        horizontalalignment='center',
        verticalalignment='center',
        transform=ax.transAxes)
        ax.set_axis_off()
    else:
        df.dropna(inplace=True)

        """ PLOTAGEM DO GRÁFICO
        O código abaixo é utilizado apenas para plotar o gráfico a partir do dataframe criado com os
        dados manipulados para a obtensão da média das avaliações de um usuário. """
        
        # Crio uma lista de categorias
        categories=list(df)[1:]

        # Obtenho o número total de categorias
        N = len(categories)
        
        # Crio uma lista com os valores das competências excluindo a coluna RA2
        # que não será necessário exibir no gráfico
        values=df.loc[0].drop('turma').values.flatten().tolist()
        values += values[:1]

        # Cria uma lista com os angulos de potagem de acordo com a quantidade de categorias
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        ax = plt.subplot(111, polar=True)
        
        # Adiciona as categorias como marcações no gráfico
        plt.xticks(angles[:-1], categories, color='grey', size=10)
        
        # Inclui a marcação de valor que cada linha representa no gráfico
        ax.set_rlabel_position(0)
        plt.yticks([10,20,30,40,50], ["1","2","3","4","5"], color="grey", size=8)
        plt.ylim(0,50)
        
        # Plota um poligno interligando os pontos de avaliação
        ax.plot(angles, values, linewidth=1, linestyle='solid')
        # Preenche a área formada pelo poligono
        ax.fill(angles, values, 'b', alpha=0.1)

    # Retorna a figura do gráfico
    return figure
