#Demonstrace, ze soucet nahodnych cisel z uniformniho
#rozdeleni jde asymptoticky k normalnimu rozdeleni

import random
from math import sqrt
from matplotlib import pyplot as plt

pocet_cisel = 10000     #celkovy pocet nahodnych cisel
pocet_scitancu = 100    #pocet cisel v souctu nahodnych cisel z uniform. roz.

normalni_rozdeleni = []
scitani_rozdeleni = []

for i in range(pocet_cisel):
    normalni_rozdeleni.append(random.gauss(0, 1))   #generovani cisla z norm. roz. 
    
    suma = 0
    for j in range(pocet_scitancu):                 #soucet cisel z Uniform(0,1)
        suma+=random.random()

    suma-=pocet_scitancu/2                          #posun sredni hodnoty na 0
    suma*=sqrt(12/pocet_scitancu)                   #skalovani sirky rozdeleni

    scitani_rozdeleni.append(suma)                  #nahodna preskalovany soucet

#histogram s nahodnymi cisly z N(0,1)
plt.hist(normalni_rozdeleni, bins = 20, range = (-4,4), histtype="step", color = "r")
#histogram s nahodnymi preskalovanymi soucty
plt.hist(scitani_rozdeleni, bins = 20, range = (-4,4), histtype="step", color = "b")
#histogramy splivaji az na statistickou chybu => Preskalovany soucet -> N(0,1)
plt.show()
