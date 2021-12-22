import random
from math import sqrt
from matplotlib import pyplot as plt

pocet_cisel = 10000

pocet_scitancu = 100

normalni_rozdeleni = []
scitani_rozdeleni = []

for i in range(pocet_cisel):
    normalni_rozdeleni.append(random.gauss(0, 1))
    
    suma = 0
    for j in range(pocet_scitancu):
        suma+=random.random()

    suma-=pocet_scitancu/2
    suma*=sqrt(12/pocet_scitancu)

    scitani_rozdeleni.append(suma)


plt.hist(normalni_rozdeleni, bins = 20, range = (-4,4), histtype="step", color = "r")
plt.hist(scitani_rozdeleni, bins = 20, range = (-4,4), histtype="step", color = "b")
plt.show()
