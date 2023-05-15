# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import db_json as dbj

# Remove a barra de feramentas do matplotlib
plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(10, 10))

def dashboard_individual(sprint, usuario):
    data = dbj.get_json_data()

    df = pd.json_normalize(data, 'Avaliacoes', ['RA1', 'Sprint'])
    df.rename(columns={'Respostas.p0': 'EPA',
                    'Respostas.p1': 'AA',
                    'Respostas.p2': 'CTE',
                    'Respostas.p3': 'CAT',
                    'Respostas.p4': 'ERVA'},
            inplace=True)

    matricula = usuario['matricula']
    df = df.query(f'RA2 == "{matricula}" and Sprint == "{sprint}"')

    df = df.groupby('RA2')[['EPA', 'AA', 'CTE', 'CAT', 'ERVA']].aggregate('mean').reset_index()
    df['EPA'] *= 10
    df['AA']  *= 10
    df['CTE'] *= 10
    df['CAT'] *= 10
    df['ERVA']*= 10

    df.dropna(inplace=True)
    
    categories=list(df)[1:]
    N = len(categories)
    
    values=df.loc[0].drop('RA2').values.flatten().tolist()
    values += values[:1]
    values
    
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    ax = plt.subplot(111, polar=True)
    
    plt.xticks(angles[:-1], categories, color='grey', size=10)
    
    ax.set_rlabel_position(0)
    plt.yticks([10,20,30,40,50], ["1","2","3","4","5"], color="grey", size=8)
    plt.ylim(0,50)
    
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    
    ax.fill(angles, values, 'b', alpha=0.1)

    plt.plot([], [], ' ', label="EPA: Engajamento e Pró-atividade")
    plt.plot([], [], ' ', label="AA: Auto-gestão das Atividades")
    plt.plot([], [], ' ', label="CTE: Comunicação e Trabalho em Equipe")
    plt.plot([], [], ' ', label="CAT: Conhecimento e Aplicabilidade Técnica")
    plt.plot([], [], ' ', label="ERVA: Entrega de Resultados com Valor Agregado")

    ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.17),
            fancybox=True, shadow=True, ncol=2)

    # Add a title
    plt.title("Sua avaliação, como você foi avaliado pelos seus colegas na Sprint 1", size=11, y=1.1)

    plt.show()