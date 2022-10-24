import csv
# pessoas = [(idade,sexo,tensão,colesterol,batimento,temDoença)]
# pessoa = (idade,sexo,tensão,colesterol,batimento,temDoença)

def lerinfo(ficheiro):
    file = open(ficheiro, "r")
    pessoas = csv.reader(file)
    listap = []
    for p in pessoas: 
        listap.append(((p[0]), p[1], p[2], p[3],p[4], p[5]))
    listap.pop(0)
    file.close()
    return listap 

#lerinfo("myheart.csv")
pessoas = lerinfo("myheart.csv")

def distribsexo(pessoas):
    distrib = {}
    for p in pessoas:
        if p[1] in distrib.keys():
            distrib[p[1]] = distrib[p[1]] + 1
        else:
            distrib[p[1]] = 1
    return distrib



# Distribuição da doença por sexo
distSexo = distribsexo(pessoas)

def distribidade():
    dicidade = {'25-29':0, '30-34': 0, '35-39':0, '40-44':0, '45-49':0, '50-54':0, '55-59':0, '60-64':0, '65-69':0, '70-74':0, '75-79':0, '80-84':0, '85-89':0, '90-94':0}
    for p in pessoas:
        valor = int(p[0])
        if valor in range(25,30):
            dicidade['25-29'] = dicidade['25-29'] + 1
        elif valor in range(30,35):
            dicidade['30-34'] = dicidade['30-34'] + 1
        elif valor in range(35,40):
            dicidade['35-39'] = dicidade['35-39'] + 1
        elif valor in range(40,45):
            dicidade['40-44'] = dicidade['40-44'] + 1
        elif valor in range(45,50):
            dicidade['45-49'] = dicidade['45-49'] + 1
        elif valor in range(50,55):
            dicidade['50-54'] = dicidade['50-54'] + 1
        elif valor in range(55,60):
            dicidade['55-59'] = dicidade['55-59'] + 1
        elif valor in range(60,65):
            dicidade['60-64'] = dicidade['60-64'] + 1
        elif valor in range(65,70):
            dicidade['65-69'] = dicidade['65-69'] + 1
        elif valor in range(70,75):
            dicidade['70-74'] = dicidade['70-74'] + 1
        elif valor in range(75,80):
            dicidade['75-79'] = dicidade['75-79'] + 1
        elif valor in range(80,85):
            dicidade['80-84'] = dicidade['80-84'] + 1
        elif valor in range(85,90):
            dicidade['85-89'] = dicidade['85-89'] + 1
        elif valor in range(90,95):
            dicidade['90-94'] = dicidade['90-94'] + 1
        
    return dicidade



# Distribuição da doença por escalões etários
distIdade = distribidade()

def mini():
    menor = int(pessoas[0][3])
    for p in pessoas:
        valor = int(p[3])
        if valor < menor:
            menor = valor
    return ("Limite inferior de colesterol: "+ str(menor))



def maxi():
    maior = int(pessoas[0][3])
    for p in pessoas:
        valor = int(p[3])
        if valor > maior:
            maior = valor
    return ("Limite superior de colesterol: "+ str(maior))



def distribcole():
    niveiscolesterol = {'0-49':0,'50-99':0,'100-149':0,'150-199':0,'200-249':0,'250-299':0,'300-349':0,'350-399':0,'400-449':0,'450-499':0,'500-549':0,'550-599':0,'600-649':0}
    for p in pessoas:
        valor = int(p[3])
        if valor in range(0,50):
            niveiscolesterol['0-49'] = niveiscolesterol['0-49'] + 1
        elif valor in range(50,100):
            niveiscolesterol['50-99'] = niveiscolesterol['50-99'] + 1
        elif valor in range(100,150):
            niveiscolesterol['100-149'] = niveiscolesterol['100-149'] + 1
        elif valor in range(150,200):
            niveiscolesterol['150-199'] = niveiscolesterol['150-199'] + 1
        elif valor in range(200,250):
            niveiscolesterol['200-249'] = niveiscolesterol['200-249'] + 1
        elif valor in range(250,300):
            niveiscolesterol['250-299'] = niveiscolesterol['250-299'] + 1
        elif valor in range(300,350):
            niveiscolesterol['300-349'] = niveiscolesterol['300-349'] + 1
        elif valor in range(350,400):
            niveiscolesterol['350-399'] = niveiscolesterol['350-399'] + 1
        elif valor in range(400,450):
            niveiscolesterol['400-449'] = niveiscolesterol['400-449'] + 1
        elif valor in range(450,500):
            niveiscolesterol['450-499'] = niveiscolesterol['450-499'] + 1
        elif valor in range(500,550):
            niveiscolesterol['500-549'] = niveiscolesterol['500-549'] + 1
        elif valor in range(550,600):
            niveiscolesterol['550-599'] = niveiscolesterol['550-599'] + 1
        elif valor in range(600,650):
            niveiscolesterol['600-649'] = niveiscolesterol['600-649'] + 1

    return niveiscolesterol


# Distribuição da doença por níveis de colesterol com intervalo de 50 unidades
distColest = distribcole()

def tabelaidade():
    dicidade = {'25-29': 4, '30-34': 17, '35-39': 53, '40-44': 88, '45-49': 107, '50-54': 168, '55-59': 172, '60-64': 135, '65-69': 65, '70-74': 23, '75-79': 7, '80-84': 0, '85-89': 0, '90-94': 0}
    valores = list(dicidade.items())
    print("Distribuição por escalões etários")
    for nivel in valores:
        print(str(nivel[0])+ " | " + str(nivel[1]))
    return



def tabdist(distribuicao):
    valores = list(distribuicao.items())
    print("Distribuição em tabela")
    for nivel in valores:
        print(str(nivel[0])+ " | " + str(nivel[1]))
    return

