#!/usr/bin/env python3
def kolik_slov(text):
    text_na_slova = text.split()    #vrati seznam retezcu - jednotlivych slov
    print(text_na_slova)            #pro ilustraci, co to dela
    pocet_slov = len(text_na_slova) #pocet slov je jeho delka
    return pocet_slov

print(kolik_slov("Zvire by bylo Baxtera odvleklo."))
