#!/usr/bin/env python3
def scitaci_vyraz(vyraz):                   #vyraz ve tvaru 123+3+45+6
    jednotliva_cisla = vyraz.split(sep="+") #rozdeli vyraz na seznam jednotlivych cisel 
    print(jednotliva_cisla)                 #POZOR, cisla jsou zapsane jako retezce (string) ne cisla (integer)
    soucet = 0
    for cislo in jednotliva_cisla:          #smycka pres vsechny cisla
        soucet += int(cislo)                #POZOR, cislo musim pretypovat na int
    return soucet

print(scitaci_vyraz("7+65+4321"))
