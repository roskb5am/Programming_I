#!/usr/bin/env python3

#Funkce, ktera vrati seznam  palindromickych slov v textu

def slova_palindromy(text):
    return [slovo for slovo in text.split() if slovo == slovo[::-1]]
    #vrati seznam vsech slov v textu rozdelenym na slova, pokud slove je stejne jako slovo pozpatku

text = "A jazykolamy mám rád. Říkám si: strč prst skrz krk"

print(slova_palindromy(text))
#vrati ['A', 'mám', 'krk']
