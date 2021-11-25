#!/usr/bin/env python3

#Funkce, ktera vrati seznam pruniku dvou (neusporadaných) seznamu

def prunik_seznamu(x, y):
    return [polozka for polozka in x if polozka in y]
    #vrati seznam vsech polozek v seznamu x, pokud polozka je i v seznamu y

seznam1 = ["banan", "pomeranc", "cokolada", 20, 14]
seznam2 = [20, "jablko", "pomeranc", 10, "pernik"]

print(prunik_seznamu(seznam1, seznam2))
#vrati ['pomeranc', 20]
