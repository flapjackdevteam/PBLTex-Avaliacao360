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

def set_respostas(sprint, usuario, usuario_avaliado, respostas, feedback):
    global data
    for avaliador in data:
        if avaliador["RA1"] == usuario["matricula"] and avaliador["Sprint"] == sprint:
            for avaliacoes in avaliador["Avaliacoes"]:
                if avaliacoes["RA2"] == usuario_avaliado["matricula"]:
                    avaliacoes["Respostas"] = respostas
                    avaliacoes["Respostas"]["feedback"] = feedback
                    return

            avaliador["Avaliacoes"].append({"RA2": usuario_avaliado["matricula"],
                                            "Nome": usuario_avaliado["nome"],
                                            "Respostas": {"feedback": feedback}})
            return

    data.append({'RA1': usuario['matricula'],
                 'Nome': usuario['nome'],
                 'Sprint': sprint,
                 'Avaliacoes': [{"RA2": usuario_avaliado["matricula"],
                                 "Nome": usuario_avaliado["nome"],
                                 "Respostas": {"feedback": feedback}}]})

def get_feedback(sprint, usuario):
    global data

    for avaliador in data:
        if (
            avaliador['Sprint'] == sprint
            and avaliador['RA1'] == 'admin'
            and avaliador['RA2'] == usuario['matricula']
        ):
            for avaliacoes in avaliador['Avaliacoes']:
                if avaliacoes['RA2'] == usuario['matricula']:
                    return avaliacoes['Respostas'].get('feedback', '')
    return ""

import json

def set_feedback(sprint, usuario, feedback):
    data = get_json_data()
    if sprint is not None:
        if sprint not in data:
            data[sprint] = {}
        data[sprint][usuario] = feedback

    salva_arquivo_json('avaliacoes.json')  

