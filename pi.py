#Vypocte pi z pomeru nahodneho rozmisteni bodu
#ve ctverci a jemu vepsanem ctvrtkruhu

import random

pocet_vsech_bodu = 1000000          #Pocet vsech bodu ve ctverci o hrane 1
pocet_do_r_jedna = 0                #Z toho pocet bodu ve ctvrtkruhu, tj. r<1

for _ in range(pocet_vsech_bodu):
    x = random.random()
    y = random.random()

    if x*x+y*y <= 1:
        pocet_do_r_jedna+=1

print("Pi je ",4*pocet_do_r_jedna/pocet_vsech_bodu)
