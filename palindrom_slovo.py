#!/usr/bin/env python3
def je_slovo_palindrom(slovo):
    otocene_slovo = slovo[::-1]     #pouziji rez s krokem -1, otoci znaky retezce
    if otocene_slovo==slovo:        #pouziji srovnani retezcu (seznamu)
        return True
    else:
        return False

print(je_slovo_palindrom("kajak"))
