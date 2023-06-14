import json

sprint = None
usuario = None
data = None

def carrega_arquivo_json(arquivo):
    global data
    with open(arquivo,'r') as f:
        data = json.loads(f.read())

def salva_arquivo_json(arquivo):
    with open(arquivo, 'w') as f:
        json.dump(data, f, indent=4)

def get_json_data():
    global data
    carrega_arquivo_json('avaliacoes.json')

    return data

def get_respostas(sprint, usuario, usuario_avaliado):
    global data
    
    for i in data:
        if i["RA1"] == usuario['matricula'] and i["Sprint"] == sprint:
            for j in i["Avaliacoes"]:
                if j["RA2"] == usuario_avaliado['matricula']:
                    return j["Respostas"]
        
    return None

def set_respostas(sprint, usuario, usuario_avaliado, respostas):
    global data

    for avaliador in data:
        if avaliador["RA1"] == usuario["matricula"] and avaliador["Sprint"] == sprint:
                for avaliacoes in avaliador["Avaliacoes"]:
                    if avaliacoes["RA2"] == usuario_avaliado["matricula"]:
                        avaliacoes["Respostas"] = respostas
                        return
                
                avaliador["Avaliacoes"].append({"RA2": usuario_avaliado["matricula"],
                                       "Nome": usuario_avaliado["nome"],
                                       "turma": usuario_avaliado["turma"],
                                       "time": usuario_avaliado["time"],
                                       "Respostas": respostas,
                                       'Feedback': ''})
                return
        
    data.append({'RA1': usuario['matricula'],
                 'Nome': usuario['nome'],
                 'Sprint': sprint,
                 'Avaliacoes': []})
    
    set_respostas(sprint, usuario, usuario_avaliado, respostas)

def get_feedback(sprint, usuario):
    global data
    feedbacks = []

    for i in data:
        if i["Sprint"] == sprint:
            for j in i["Avaliacoes"]:
                if j["RA2"] == usuario['matricula']:
                    feedbacks.append(j["Feedback"])
                
    return feedbacks

def get_qtd_de_sprints():
    global data
    carrega_arquivo_json('data.json')
    return data['admin']['qtd_sprints']

def set_qtd_de_sprints(qtd_sprints):
    global data
    carrega_arquivo_json('data.json')
    data['admin']['qtd_sprints'] = qtd_sprints
    salva_arquivo_json('data.json')

def get_times():
    global data
    times = []
    carrega_arquivo_json('data.json')

    for i in data['usuarios']:
        if i['time'] not in times:
            times.append(i['time'])

    return times

def get_turmas():
    global data
    turmas = []
    carrega_arquivo_json('data.json')

    for i in data['usuarios']:
        if i['turma'] not in turmas:
            turmas.append(i['turma'])

    return turmas

def ra_exist(ra):
    global data
    carrega_arquivo_json('data.json')

    for i in data['usuarios']:
        if i['matricula'] == ra:
            return True
    
    return False