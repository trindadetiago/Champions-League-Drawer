import Saves
import random
Teams = Saves
class Time:
    def __init__(self, nome, pais, chave, escudo):
        self.nome = nome
        self.pais = pais
        self.chave = int(chave)
        self.escudo = escudo
grupos = []
def draw():

    times = Teams.TeamsDic
    timeslist = Teams.TeamsList

    chave1 = []
    chave2 = []
    chave3 = []
    chave4 = []
    chaves = [chave1, chave2, chave3, chave4]

    grupoA = []
    grupoB = []
    grupoC = []
    grupoD = []
    grupoE = []
    grupoF = []
    grupoG = []
    grupoH = []
    global grupos
    grupos = [grupoA, grupoB, grupoC, grupoD, grupoE, grupoF, grupoG, grupoH]
    gruposList = ["grupoA", "grupoB", "grupoC", "grupoD", "grupoE", "grupoF", "grupoG", "grupoH"]
    gruposDic = {"grupoA": grupoA, "grupoB": grupoB, "grupoC": grupoC, "grupoD": grupoD,
                 "grupoE": grupoE, "grupoF": grupoF, "grupoG": grupoG, "grupoH": grupoH}


    for i in range(32):
        t = timeslist[i]
        if times[t].chave == 1:
            chave1.append(t)
        if times[t].chave == 2:
            chave2.append(t)
        if times[t].chave == 3:
            chave3.append(t)
        if times[t].chave == 4:
            chave4.append(t)

    for chaveX in chaves:
        for time in chaveX:
            grupos_disponiveis = ["grupoA", "grupoB", "grupoC", "grupoD", "grupoE", "grupoF", "grupoG", "grupoH"]
            for gp in gruposList:
                if gruposDic[gp].__len__() != 0:
                    for team in gruposDic[gp]:
                        if times[team].pais == times[time].pais or times[team].chave == times[time].chave:
                            if gp in grupos_disponiveis:
                                grupos_disponiveis.remove(gp)

            number = random.randint(0, grupos_disponiveis.__len__()-1)
            gruposDic[grupos_disponiveis[number]].append(time)



    #for g in grupos:
        #print(g)
def Sortear():
    try: draw()
    except: Sortear()