import random

def fejiras():
    fejiras_lista=[]
    print("II/A, B, C:")
    i:int=1
    while (i <= 7):
        dobas:int = int(random.randint(0,1))
        fejiras_lista.append(dobas)
        if dobas == 0:
            if i == 7:
                print("FEJ")
            else:
                print("FEJ", end="-")
        elif dobas == 1:
            if i == 7:
                print("ÍRÁS")
            else:
                print("ÍRÁS", end="-")
        i += 1
    return fejiras_lista

def fejek_szama(fejiras_lista):
    f:int = 0
    for i in range(0, len(fejiras_lista),1):
        if fejiras_lista[i] == 0:
            f += 1
    return f

def konzol_kiir(f):
    print("II/D, E:")
    print(f"A fejek száma: {f}.")

def file_kiir(f):
    fajlom = open("fejek.txt", "w", encoding="UTF-8")
    
    fajlom.write("II/F\n")
    fajlom.write(f"A fejek száma: {f}.")
    fajlom.close()

