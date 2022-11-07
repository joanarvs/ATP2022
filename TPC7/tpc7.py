import csv
import matplotlib.pyplot as plt
# Alunos = [(id,nome,curso,tpc1,tpc2,tpc3,tpc4)]

def lerDataset():
    file = open("alunos.csv", encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter=",")
    alunos = []
    for aluno in csv_file:
        alunos.append(tuple(aluno))
    file.close
    return alunos

def distCurso(alunos):
    dici = {}
    for id, nome, curso, *_ in alunos:
        if curso in dici.keys():
            dici[curso] = dici[curso] + 1
        else:
            dici[curso] = 1
    distCurso = sorted(dici.items(), key = lambda x: x[0])
    novoDici = dict(distCurso)
    return novoDici

def mediaNotas(alunos):
    for aluno in alunos:
        id,_,_,tpc1,tpc2,tpc3,tpc4 = aluno
        media = (int(tpc1) + int(tpc2) + int(tpc3) + int(tpc4))/4
        al = list(aluno)
        al.append(media)
        alunoNovo = tuple(al)
        alunos[alunos.index(aluno)] = alunoNovo
    return alunos

def escaloesNotas(alunos):
    alunosmed = mediaNotas(alunos)
    for aluno in alunosmed:
        id,_,_,_,_,_,_, media = aluno
        novoA = list(aluno)
        if 1 <= media < 5:
            escalao = 'E'
        elif 5 <= media < 9:
            escalao = 'D'
        elif 9 <= media < 13:
            escalao = 'C'
        elif 13 <= media < 17:
            escalao = 'B'
        elif 17 <= media <= 20:
            escalao = 'A'
        novoA.append(escalao)
        aNovo = tuple(novoA)
        alunosmed[alunosmed.index(aluno)] = aNovo
    return alunosmed

def distEscalao(alunos):
    dici = {}
    alunosEscalao = escaloesNotas(alunos)
    for id, _, _, _, _, _, _, _, escalao in alunosEscalao:
        if escalao in dici.keys():
            dici[escalao] = dici[escalao] + 1
        else:
            dici[escalao] = 1
    distEscaloes = sorted(dici.items(), key = lambda x: x[0])
    novoDici = dict(distEscaloes)
    return novoDici

def grafDist(dist):
    plt.plot(dist.keys(), dist.values(), marker='o', markerfacecolor='blue', markersize=5)
    plt.show()
    return

def tabelaDist(dist):
    print(f"|{'Distribuição em tabela':^25}|")
    print(f' {"-":-^25}')
    for key, value in dist.items():
        print(f"|{key:^10} |{value:^12} |") 
    return

def qualDist(alunos):
    dist = int(input("Prima 2 para dist. por curso ou prima 5 para dist. por escalão"))
    if dist == 2:
        print(grafDist(distCurso(alunos)))
    elif dist == 5:
        print(grafDist(distEscalao(alunos)))
    else:
        print("Input inválido")
    return

def qualDistTab(alunos):
    dist = int(input("Prima 2 para dist. por curso ou prima 5 para dist. por escalão"))
    if dist == 2:
        print(tabelaDist(distCurso(alunos)))
    elif dist == 5:
        print(tabelaDist(distEscalao(alunos)))
    else:
        print("Input inválido")
    return

def programa():
    menu ="""Menu:
1.Ler o Dataset
2.Distribuição dos alunos por curso
3.Dataset com a média das notas de cada aluno
4.Dataset com o escalão das notas
5.Distribuição dos alunos por escalão
6.Distribuição em gráfico de linhas
7.Distribuição em tabela
0.Sair """
    print(menu)
    alunos = []
    option = int(input("Selecione uma opção"))
    while option in range(1,8):
        if option == 1:
            alunos = lerDataset()
            #print(alunos)
        elif option == 2:
            print(distCurso(alunos))
        elif option == 3:
            print(mediaNotas(alunos))
        elif option == 4:
            print(escaloesNotas(alunos))
        elif option == 5:
            print(distEscalao(alunos))
        elif option == 6:
            print(qualDist(alunos))
        elif option == 7:
            print(qualDistTab(alunos))
        print(menu)
        option = int(input("Selecione uma opção"))
    if option == 0:
        print("Terminou")
    return