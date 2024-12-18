class Helyzet:
    def __init__(self, id, hely, tipus, ipcim):
        self.id = int(id)
        self.hely = hely
        self.tipus = tipus
        self.ipcim = ipcim

    def __str__(self):
        return f"ID: {self.id}, Hely: {self.hely}, Típus: {self.tipus}, IP: {self.ipcim}"

def beolvasas(fajlnev):
    gepek = []
    file = open(fajlnev, "r")
    sorok = file.readlines()
    file.close()
    fejléc = sorok[0]
    for i in range(1, len(sorok)):
        id, hely, tipus, ipcim = sorok[i].strip().split("!")
        gepek.append(Helyzet(id, hely, tipus, ipcim))
    return gepek

def gepek_szama(gepek):
    print("III/A, B:")
    print(f"A gépek száma: {len(gepek)}.")

def atlag(gepek):
    paros_terem_azonositok = []
    for i in range(len(gepek)):
        gep = gepek[i]
        if int(gep.hely[1:]) % 2 == 0:
            paros_terem_azonositok.append(gep.id)
    if len(paros_terem_azonositok) > 0:
        atlag = sum(paros_terem_azonositok) / len(paros_terem_azonositok)
        print(f"III/C:\nA páros teremszámú termek azonosító átlaga: {atlag:.2f}.")
    else:
        print("III/C:\nNincs páros teremszámú terem.")

def legkisebb(gepek):
    asztali_gepek = []
    for i in range(len(gepek)):
        gep = gepek[i]
        if gep.tipus == "asztali":
            asztali_gepek.append(gep)
    if len(asztali_gepek) > 0:
        legkisebb_gep = asztali_gepek[0]
        for j in range(len(asztali_gepek)):
            gep = asztali_gepek[j]
            if gep.id < legkisebb_gep.id:
                legkisebb_gep = gep
        print(f"III/D:\nA legkisebb asztali gép azonosítója: {legkisebb_gep.id}, helye: {legkisebb_gep.hely}.")
    else:
        print("III/D:\nNincs asztali gép.")
