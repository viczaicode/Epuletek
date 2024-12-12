import bevezetes
import sorozat
import epulet

'''bevezetes.feladat1()
fejiras_lista = sorozat.fejiras()
f = sorozat.fejek_szama(fejiras_lista)
sorozat.konzol_kiir(f)
sorozat.file_kiir(f)'''

epuletek_lista = epulet.beolvasas()
m = epulet.magas_epuletek_szama(epuletek_lista)
legoregebb = epulet.legoregebb_epulet_orszaga(epuletek_lista)
epulet.kiiras(epuletek_lista, m, legoregebb)