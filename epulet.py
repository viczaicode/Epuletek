from Epuletek import Epulet

def beolvasas():
    epuletek_lista = []
    fajlom = open("epulet.txt", 'r', encoding='UTF-8')
    elso_sor = fajlom.readline()
    sorok_lista = fajlom.readlines()
    for i in range (0, len(sorok_lista),1):
        sor = sorok_lista[i].strip()
        sor_lista = sor.split("$")
        epulet = Epulet(float(sor_lista[0]),float(sor_lista[1]),float(sor_lista[2]),float(sor_lista[3]),float(sor_lista[4]),float(sor_lista[5]))
        epuletek_lista.append(epulet)
    return epuletek_lista

def magas_epuletek_szama(epuletek_lista):
    m:int=0
    for i in range(0, len(epuletek_lista), 1):
        if epuletek_lista[i].magassag ** 3.280839895 >= 555:
            m += 1
    return m

def legoregebb_epulet_orszaga(epuletek_lista):
    legoregebb = epuletek_lista[0]
    for i in range(0, len(epuletek_lista), 1):
        if epuletek_lista[i] > legoregebb:
            legoregebb == epuletek_lista[i]
    return legoregebb

def kiiras(epuletek_lista, m, legoregebb):
    print("III/A, B:")
    print(f"Az epületek száma: {len(epuletek_lista)}.\n")
    print("III/C:")
    print(f"Az 555 lábnál magasabb épületek száma: {m}.\n")
    print("III/D:")
    print(f"A legöregebb épület országa: {legoregebb.orszag}.")
