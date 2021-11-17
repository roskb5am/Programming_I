#!/usr/bin/env python3
def je_veta_palindrom(veta):
    veta_na_slova = veta.split()                            #abych odstranil mezery, rozdelim vetu na slova
    print(veta_na_slova)
    veta_jako_jedno_slovo = "".join(veta_na_slova)          #slova spojim s nulovym znakem, vznikne jedno slovo
    print(veta_jako_jedno_slovo)

    if veta_jako_jedno_slovo==veta_jako_jedno_slovo[::-1]:  #stejne jako pro slovo
        return True
    else:
        return False

print(je_veta_palindrom("kobyla ma maly bok"))
