import random

def veletlen():
    lista = []
    for i in range(0,15,1):
        szam = random.randint(-90,500)
        lista.append(szam)
    return lista

def oszthatok_szama(lista):
    tizzeloszthatok = 0
    for i in range(0,15,1):
        if (lista[i] % 10):
            tizzeloszthatok += 1
    return tizzeloszthatok

def konzolra_kiir(lista,tizzel):
    print("II/A, B, C:")
    print(*lista,sep="*")
    print("II/D, E:")
    print(f"Tízzel osztható számok száma: {tizzel}")

def fajl_ir(tizzel):
    f = open("kimutatas.txt","a")
    f.write(f"Tízzel osztható számok száma: {tizzel}.")