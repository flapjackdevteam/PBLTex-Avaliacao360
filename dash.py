import json
import matplotlib.pyplot as plt

# Carregar os dados do arquivo json
with open('avaliacoes.json') as file:
    data = json.load(file)

# Definir qual competência está sendo analizada
competencia = 'p0'

# Definir o usuário a ser analizado
user_ra = 'RA12345'  # Substituir pelo RA do usuário desejado

#Criar um dicionário para guardar as respostas por sprint
ratings_por_sprint = {1: [], 2: [], 3: [], 4: []}

# Agregar as respostas por sprint e competência
for sprint_data in data.values():
    for sprint, avaliacoes in sprint_data.items():
        if sprint.startswith('Sprint '):
            for avaliacao in avaliacoes.values():
                if avaliacao.get('tipo') == 'individual':
                    nota = avaliacao['respostas'].get(competencia)
                    if nota is not None:
                        ratings_por_sprint[int(sprint[-1])].append(nota)

# Calcular a média das respotas para cada sprint
medias_por_sprint = {sprint: sum(ratings) / len(ratings) for sprint, ratings in ratings_por_sprint.items()}

# Criar um Dashboard em barra para exibir os resultados
plt.bar(medias_por_sprint.keys(), medias_por_sprint.values())
plt.xlabel('Sprint')
plt.ylabel('Média')
plt.title(f'Média das respostas da avaliação 360º na competência {competencia} por sprint')
plt.xticks(list(medias_por_sprint.keys()), ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4'])
plt.yticks(range(1, 6))
plt.show()
