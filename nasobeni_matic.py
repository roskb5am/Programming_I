#!/usr/bin/env python3

#Funkce, ktera vrati skalarni soucin dvou vektoru

def skal_soucin(a,b):
    return sum([x_a*x_b for x_a, x_b in zip(a, b)])
    #vrati soucet vsech polozek seznamu
    #kde seznam tvori soucin soucin dvojic
    #kde kazda dvojice je i-ta polozka z kazdeho vektoru

#Funkce, ktera vrati transponovanou matici

def transpozice_matice(m):
    return [[a[i] for a in m] for i in range(len(m[0]))]
    #vytvori seznam seznamu
    #kde kazdy podseznam obsahuje i-ty element a-teho radku m
    #kde i je index i-teho sloupce m, tj. bezi az do delky radku m

#Funkce, vynasobi matice m1 a m2, tj. m = m1.m2
#Funkce vyuziva skutecnosti, ze elemet vysledne matice m[i][j] je
#skalarni soucin i-teho radku m1 a j-teho radku m2_trans, transponovane m2

def nasobeni_matic(m1, m2):
    m2t = transpozice_matice(m2)
    return [[skal_soucin(radek_m1, radek_m2t) for radek_m2t in m2t] for radek_m1 in m1]
    #vrati seznam seznamu
    #kde podseznam je radek vysledne matice
    #i-ty element podseznamu je dan jako skalarni soucin radku m1 s i-tym radkem m2t
    #rozmysli si, ze proto je prvni for cyklus pres radky m2t, ne pres radky m1!!!

m1 = [[2, 1], [1, 1]]
m2 = [[3, 2], [4, 1]]

print(nasobeni_matic(m1,m2))
#vrati [[10, 5], [7, 3]]
