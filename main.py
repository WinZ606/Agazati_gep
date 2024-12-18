import minosites
import sorozat
from Helyzet import Helyzet
import Helyzet

minosites.visszajelzes(minosites.adatbekeres())
sorozat.konzolra_kiir(sorozat.veletlen(),sorozat.oszthatok_szama(sorozat.veletlen()))
sorozat.fajl_ir(sorozat.oszthatok_szama(sorozat.veletlen()))
gepek = Helyzet.beolvasas("gep.txt")
Helyzet.gepek_szama(gepek)
Helyzet.atlag(gepek)
Helyzet.legkisebb(gepek)