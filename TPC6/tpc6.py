# Modelo = [(nome, desc, ano, periodo, compositor, duração, _id)]
import csv
import matplotlib.pyplot as plt

def lerObras():
    file = open("obras.csv", encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter=";")
    obras = []
    for linha in csv_file:
        obras.append(tuple(linha))
    file.close
    return obras

def contaObras(obras):
    return len(obras)

def imprimeObras(obras):
    print(f"| {'Título':20} | {'Descrição':25} | {'Compositor':20} | {'Ano':5} |")
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {compositor[:20]:20} | {ano:5} |")
    
def ordemtuplos(t):
    return t[0]

def titAno(obras):
    list = []
    for obra in obras:
        list.append((obra[0], obra[2]))
    list.sort(key= ordemtuplos)
    return list

def titAno2(obras):
    list = []
    for obra in obras:
        list.append((obra[0], obra[2]))
    list.sort(key = lambda tuplo: tuplo[1])
    return list

#Distribuição das obras por ano
#def titporAno(obras):
#    dici = {}
#    for nome, _, ano, *_ in obras:
#        if ano in dici.keys():
#            dici[ano].append(nome)
#        else:
#            dici[ano] = [nome]
#    return dici

def listComp(obras):
    lista = []
    for obra in obras:
        if obra[4] not in lista:
            lista.append(obra[4])
    lista.sort()
    return lista

def distPeriodo(obras):
    dici = {}
    for _, _, _, periodo, *_ in obras:
        if periodo in dici.keys():
            dici[periodo] = dici[periodo] + 1
        else:
            dici[periodo] = 1
    return dici    

def distAno(obras):
    dici = {}
    for nome, _, ano, *_ in obras:
        if ano in dici.keys():
            dici[ano] = dici[ano] + 1
        else:
            dici[ano] = 1
    return dici 

def distComp(obras):
    dici = {}
    for nome, desc, ano, _, comp, *_ in obras:
        if comp in dici.keys():
            dici[comp] = dici[comp] + 1
        else:
            dici[comp] = 1
    return dici

def plotDistrib(distrib):
    plt.bar(distrib.keys(), distrib.values(), width = 0.4)
    plt.xticks([x for x in range(0, len(distrib.keys()))], distrib.keys(), rotation='vertical')
    plt.rcParams["figure.figsize"] = (20,4)
    plt.xlim(-0.4,len(distrib.keys()))
    plt.show()
    return

# Estrutura de dados
# lcomp = {comp: [titulos]}

def estDados(obras):
    lcomp = {}
    for titulo, desc, ano, _, comp, *_ in obras:
        if comp not in lcomp.keys():
            lcomp[comp] = []
        if titulo not in lcomp[comp]:
            lcomp[comp].append(titulo)
    return lcomp

