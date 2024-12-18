def adatbekeres():
    print("I/A:")
    lista = []
    muzeum_neve = input("Múzeum neve: ")
    latogato_neve = input("Látogató neve: ")
    ertekeles = int(input("Értékelés (1-20): "))
    lista.append(muzeum_neve)
    lista.append(latogato_neve)
    lista.append(ertekeles)
    return lista

def visszajelzes(lista):
    print("I/B:")
    if (lista[2] > 20):
       print("20 pont feletti értékelés nem elfogadható!")
    elif (lista[2] < 1):
        print("Az értékelés nem lehet negatív vagy 0!")
    else:
        print("Köszönjük az értékelést!")