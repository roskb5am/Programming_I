#!/usr/bin/env python3
def kolik_ruznych_slov(text):
    text_na_slova = text.split()                #rozdeli text na seznam retezcu slov

    seznam_ruznych_slov = []                    #sem vkladam slova, kazde ale jen jednou, takze budou ruzna

    for slovo in text_na_slova:                 #smycka pres vsechny slova v textu
        if slovo not in seznam_ruznych_slov:    #pokud slovo neni v seznamu ruznych slov
            seznam_ruznych_slov.append(slovo)   #pridam ho
        else:                                   #jinak
            pass                                #nedelam nic
    return len(seznam_ruznych_slov)             #pocet ruznych slov je delka seznamu
 

print(kolik_ruznych_slov("a zvire by bylo Baxtera odvleklo, nebyli by Gordon, Wilcox a Service rychle nezasahli"))
