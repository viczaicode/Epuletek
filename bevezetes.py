def feladat1():
    print("I/A:")
    nev:str = str(input("Játékos neve: "))
    szerepkor:str = str(input("szerepkör:\n"))
    print("I/B:")
    if (nev == "varázsló"):
        print(f"Üdvözlünk {nev}, 2 életed van!")
    elif (nev == "harcos"):
        print(f"Üdvözlünk {nev}, 10 életed van!")
    else:
        print(f"Üdvözlünk {nev}, 8 életed van!")