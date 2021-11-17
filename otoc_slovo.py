#!/usr/bin/env python3
def otoc_slovo(slovo):
    otocene_slovo = slovo[::-1]     #pouziji rez s krokem -1, otoci znaky retezce
    return otocene_slovo

print(otoc_slovo("abrakadabra"))
