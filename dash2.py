import matplotlib.pyplot as plt
import numpy as np
import json

# Load JSON data from file
with open("avaliacoes.json", "r") as file:
    data = json.load(file)

# Extrair dados
sprints = []
questions = []
individual_scores = {}
RA = {}
sprintsx = ['Sprint 1', "Sprint 2", "Sprint 3", "Sprint 4"]

for RA, sprint_data in data.items():
    for sprint_name, sprint_details in sprint_data.items():
        if sprint_name not in sprints:
            sprints.append(sprint_name)
        for RA, RA_details in sprint_details.items():
            if RA not in individual_scores:
                individual_scores[RA] = [0] * 5
            if isinstance(RA_details, dict) and 'respostas' in RA_details:
                respostas = RA_details['respostas']
                for i in range(5):
                    question = f'p{i}'
                    if question in respostas:
                        individual_scores[RA][i] = respostas[question]

# Calculate aveRAge scores
average_scores = np.mean(list(individual_scores.values()), axis=0)

# Create bar chart
x = np.arange(5)
width = 0.35

fig, ax = plt.subplots()
individual_bars = ax.bar(x, average_scores, width)

# Set labels, title, and ticks
ax.set_xlabel('Respostas')
ax.set_ylabel('Média das Respostas')
ax.set_title('AveRAge Scores by Question (Individual)')
ax.set_xticks(x)
ax.set_xticklabels(['p0', 'p1', 'p2', 'p3', 'p4'])

# Display the chart
plt.show()
